from sqlalchemy.orm import relationship
from app.config.db import db

class Producto_Ingrediente(db.Model):
    __tablename__ = "producto_Ingrediente"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable= False)
    producto_id = db.Column(db.Integer, db.ForeignKey ('productos.id'), nullable= False)
    ingrediente_id =  db.Column (db.Integer, db.ForeignKey ('ingredientes.id'), nullable= False)

    producto = relationship("Producto", back_populates="producto_ingredientes")
    ingrediente = relationship("Ingrediente", back_populates="ingrediente_productos")

    @classmethod
    def create_test_conections(cls):
        if not cls.query.first():
            dummy_connections = [
                Producto_Ingrediente(id = 1 , producto_id = 1 , ingrediente_id = 2),
                Producto_Ingrediente(id = 2 , producto_id = 1 , ingrediente_id = 6),
                Producto_Ingrediente(id = 3 , producto_id = 1 , ingrediente_id = 10),
                Producto_Ingrediente(id = 4 , producto_id = 2 , ingrediente_id = 3),
                Producto_Ingrediente(id = 5 , producto_id = 2 , ingrediente_id = 4),
                Producto_Ingrediente(id = 6 , producto_id = 3 , ingrediente_id = 5),
                Producto_Ingrediente(id = 7 , producto_id = 3 , ingrediente_id = 1),
                Producto_Ingrediente(id = 8 , producto_id = 3 , ingrediente_id = 8),
                Producto_Ingrediente(id = 9 , producto_id = 4 , ingrediente_id = 9),
                Producto_Ingrediente(id = 10 , producto_id = 4 , ingrediente_id = 7),
                Producto_Ingrediente(id = 11 , producto_id = 4 , ingrediente_id = 5)
            ]
            db.session.bulk_save_objects(dummy_connections)
            db.session.commit()