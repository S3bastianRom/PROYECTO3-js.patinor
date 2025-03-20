from flask import Flask
from app.config.config import Config
from app.config.config import SK
from app.config.db import db
from app.config.routes import register_routes

from app.config.db import db
from app.models.ingrediente import Ingrediente
from app.models.producto import Producto
from app.models.producto_ingrediente import Producto_Ingrediente
from app.models.heladeria import Heladeria
from app.models.usuario import Usuario
from app.config.auth import login_manager

app = Flask(__name__, template_folder="app/views", static_folder="app/static")
app.config.from_object(Config)
app.config.from_object(SK)
login_manager.init_app(app)
db.init_app(app)
register_routes(app)

with app.app_context():
    db.drop_all()
    db.create_all()

    Heladeria.create_test_heladeria()
    Producto.create_test_products()
    Ingrediente.create_test_ingredientes()
    Producto_Ingrediente.create_test_conections()
    Usuario.create_test_users()


if __name__ == "__main__":
    app.run(debug=True)