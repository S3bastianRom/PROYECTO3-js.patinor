from flask import Blueprint, render_template, flash, redirect, url_for, jsonify
from flask_login import login_user, logout_user, login_required, current_user, UserMixin
from app.config.db import db
from app.models.ingrediente import Ingrediente
from app.models.producto import Producto
from app.models.producto_ingrediente import Producto_Ingrediente
from app.models.heladeria import Heladeria
from app.utils.decorators import roles_required

ventas_bp = Blueprint ("ventas", __name__, url_prefix= "/ventas")

#Modulo ventas
@ventas_bp.route("/")
@roles_required("cliente", "empleado", "admin")
def ventas():
    productos = Producto.query.all()
    return render_template("ventas.html", productos = productos)

#Ventas HTML
@ventas_bp.route("/vender/<string:nombre>")
@roles_required("cliente", "empleado", "admin")
def vender(nombre):
    heladeria = Heladeria.query.first()

    try:
        heladeria.vender(nombre)
        db.session.commit()
        flash("¡Vendido!", "success")
    except ValueError as e:
        db.session.rollback()
        flash(f"¡Oh no! Nos hemos quedado sin {str(e)}", "danger")

    return redirect(url_for("ventas.ventas"))

#Mejor productop HTML
@ventas_bp.route("/mejor_producto")
@roles_required("empleado", "admin")
def mejor_producto ():
    heladeria = Heladeria.query.first()

    try:
        mejor = heladeria.obtener_mejor_producto()
        flash(f"El producto más rentable es: {mejor}", "success")
    except ValueError as e:
        flash(str(e), "danger")

    return redirect(url_for("index.ventas"))