from flask import Blueprint, render_template, flash, redirect, url_for, jsonify
from flask_login import login_user, logout_user, login_required, current_user, UserMixin
from app.config.db import db
from app.models.ingrediente import Ingrediente
from app.models.producto import Producto
from app.models.producto_ingrediente import Producto_Ingrediente
from app.models.heladeria import Heladeria
from app.utils.decorators import roles_required

admin_bp = Blueprint ("admin", __name__, url_prefix= "/administracion")

@admin_bp.route("/")
@roles_required("cliente", "empleado", "admin")
def administracion():
    ingredientes  = Ingrediente.query.all()
    productos  = Producto.query.all()
    return render_template("administracion.html", ingredientes =  ingredientes, productos = productos)

#Ingredientes
#Es sano HTML
@admin_bp.route("/es_sano/<int:id>")
@roles_required("empleado", "admin")
def es_sano(id):
    ingrediente = Ingrediente.query.filter_by(id=id).first()
    
    try:
        sano = ingrediente.es_sano()
        flash(f"El ingrediente {ingrediente.nombre} es sano: {sano}", "success")
    except ValueError as e:
        flash(f"El ingrediente {ingrediente.nombre} es sano: {e}", "danger")

    return redirect(url_for("admin.administracion"))

#Abastecer HTML
@admin_bp.route("/abastecer/<int:id>")
@roles_required("empleado", "admin")
def abastecer(id):
    ingrediente = Ingrediente.query.filter_by(id=id).first()
    
    try:
        ingrediente.abastecer()
        db.session.commit()
        flash(f"El complemento {ingrediente.nombre} ha sido abastecido, ahora el {ingrediente.nombre} tiene {ingrediente.inventario}", "success")
    except:
        db.session.commit()
        flash(f"La base {ingrediente.nombre} ha sido abastecido, ahora el {ingrediente.nombre} tiene {ingrediente.inventario}", "success")


    return redirect(url_for("admin.administracion"))

#Renovar complementos HTML
@admin_bp.route("/renovar_complementos/<int:id>")
@roles_required("empleado", "admin")
def renovar_complementos(id):
    ingrediente = Ingrediente.query.filter_by(id=id).first()
    
    try:
        ingrediente.renovar_inventario()
        db.session.commit()
        flash(f"El complemento {ingrediente.nombre} ha sido renmovado, ahora tienes {ingrediente.inventario}", "success")
    except ValueError as e:
        flash (f"El producto {str(e)} es base y no se puede renovar", "danger")

    return redirect(url_for("admin.administracion"))

#Productos
#Calcular calorias HTML
@admin_bp.route("/calcular_calorias/<int:id>")
@roles_required("cliente", "empleado", "admin")
def calcular_calorias(id):
    producto = Producto.query.filter_by(id=id).first()
    
    total = producto.calcular_calorias()
    flash(f"El total de calorias es {total}", "success")

    return redirect(url_for("admin.administracion"))

#Costo produccion HTML
@admin_bp.route("/costo_produccion/<int:id>")
@roles_required("empleado", "admin")
def costo_produccion(id):
    producto = Producto.query.filter_by(id=id).first()

    total_costo = producto.calcular_costo()
    flash(f"El costo de produccion es {total_costo}", "success")

    return redirect(url_for("admin.administracion"))

#Calculo rentabilidad HTML
@admin_bp.route("/calcular_rentabilidad/<int:id>")
@roles_required("admin")
def calcular_rentabilidad(id):
    producto = Producto.query.filter_by(id=id).first()

    total_rentabilidad = producto.calcular_rentabilidad()
    flash(f"La rentabilidad de este producto {total_rentabilidad}", "success")

    return redirect(url_for("admin.administracion"))