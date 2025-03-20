from flask import Blueprint, render_template, flash, redirect, url_for, jsonify
from flask_login import login_user, logout_user, login_required, current_user, UserMixin
from app.config.db import db
from app.models.ingrediente import Ingrediente
from app.models.producto import Producto
from app.models.producto_ingrediente import Producto_Ingrediente
from app.models.heladeria import Heladeria
from app.utils.decorators import roles_required

index_bp = Blueprint ("index", __name__, url_prefix= "/index")

#Index
@index_bp.route("/")
def index():
    if current_user.is_authenticated:
        if current_user.es_admin:
            return redirect(url_for('index.home_admin'))
        elif current_user.es_empleado:
            return redirect(url_for('index.home_employee'))
        elif current_user.es_cliente:
            return redirect(url_for('index.home_employee'))
    else:
        return redirect(url_for('index.home_non_user'))
        

#Menu de comida HTML
@index_bp.route("/menu")
def menu():
    productos = Producto.query.all()
    return render_template("menu.html", productos = productos)

#Admin home HTML
@index_bp.route("home_admin")
@roles_required("admin")
def home_admin():
    return render_template("home_admin.html", current_user = current_user)

#Employee home HTML
@index_bp.route("home_employee")
@roles_required("empleado")
def home_employee():
    return render_template("home_employees.html", current_user = current_user)

#Non user home HTML
@index_bp.route("home_non_user")
def home_non_user():
    return render_template("home_non_user.html", current_user = current_user)