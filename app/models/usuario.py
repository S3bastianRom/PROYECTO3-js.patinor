from app.config.db import db
from flask_login import UserMixin

class Usuario(db.Model, UserMixin):
    __tablename__ ='usuario'
    #PK
    id = db.Column(db.Integer, primary_key = True, nullable = False ,autoincrement = True)
    #Columns
    username = db.Column (db.String(500))
    password  = db.Column (db.String(500))
    es_admin = db.Column (db.Boolean)
    es_empleado = db.Column (db.Boolean)
    es_cliente = db.Column (db.Boolean)


    @classmethod
    def create_test_users(cls):
        if not cls.query.first():
            users = [
                cls(username="admin", password=("admin123"),        es_admin = True, es_empleado = False, es_cliente = False),
                cls(username="empleado", password=("empleado123"),  es_admin = False, es_empleado = True, es_cliente = False),
                cls(username="cliente", password=("cliente123"),    es_admin = False, es_empleado = False, es_cliente = True)
            ]
            db.session.bulk_save_objects(users)
            db.session.commit()