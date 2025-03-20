from functools import wraps
from flask import redirect, url_for, flash, jsonify
from flask_login import current_user

from functools import wraps
from flask import redirect, url_for, flash
from flask_login import current_user

def roles_required(*roles):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.is_authenticated:
                flash("Debes iniciar sesión para acceder.", "warning")
                return redirect(url_for("login.login"))

            # Verificar si el usuario tiene al menos uno de los roles requeridos
            if not any(getattr(current_user, f"es_{role}", False) for role in roles):
                flash("No autorizado", "danger")
                return redirect(url_for("index.index"))

            return f(*args, **kwargs)
        return decorated_function
    return decorator


def api_roles_required(*roles):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.is_authenticated:
                return jsonify ({"Sin sesion activa"}),401

            if not any(getattr(current_user, f"es_{role}", False) for role in roles):
                return jsonify ({"No autorizado"}),401

            return f(*args, **kwargs)
        return decorated_function
    return decorator
