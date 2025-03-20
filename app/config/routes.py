from app.controllers.index import index_bp
from app.controllers.adminstracion import admin_bp
from app.controllers.ventas import ventas_bp
from app.controllers.login import login_bp
from app.controllers.api import api_bp


def register_routes(app):
    app.register_blueprint(index_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(ventas_bp)
    app.register_blueprint(login_bp)
    app.register_blueprint(api_bp)