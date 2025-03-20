from app.config.auth import login_manager
from app.models.usuario import Usuario
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user, UserMixin
from werkzeug.security import check_password_hash

login_bp = Blueprint("login", __name__, url_prefix="/login")

@login_required
@login_manager.user_loader
def load_user(user_id:int):
    return Usuario.query.get(int(user_id))

#Login based on profile
@login_required
@login_bp.route("/")
def login():
    if current_user.is_authenticated:
        flash ("Ya tienes una sesion activa", "info")

        if current_user.es_admin:
            return redirect(url_for('index.home_admin'))
        elif current_user.es_empleado:
            return redirect(url_for('index.home_employee'))
        elif current_user.es_cliente:
            return redirect(url_for('index.home_employee'))
        else:    
            return redirect(url_for('index.home_non_user'))
    else:
        return render_template ('login.html')

@login_required
@login_bp.route("/auth")
def auth ():
    username = request.args.get("username")
    password = request.args.get("password")

    user = Usuario.query.filter_by (username=username, password=password).first()

    if user:
        login_user(user)
        flash ("Sesion iniciada exitosamente", "success")

        if user.es_admin:
            return redirect(url_for('index.home_admin'))
        elif user.es_empleado:
            return redirect(url_for('index.home_employee'))
        elif user.es_cliente:
            return redirect(url_for('index.home_employee'))
        else:
            return redirect(url_for('index.home_non_user'))
    else:
        flash ("Credenciales incorrectas, revisa", "warning")
        return redirect(url_for('login.login'))


@login_bp.route("/logout")
def logout():
    logout_user()
    flash ("Has sido desloggeado", "info")
    return redirect(url_for('index.home_non_user'))