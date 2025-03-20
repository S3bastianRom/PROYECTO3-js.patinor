from sqlalchemy.orm import relationship
from app.config.db import db
from funciones import esto_es_sano
class Ingrediente(db.Model):
    __tablename__ = "ingredientes"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable= False)
    nombre = db.Column(db.String(100), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    calorias = db.Column(db.Float, nullable=False)
    inventario = db.Column(db.Float, nullable=False)
    es_vegetariano = db.Column(db.Boolean, nullable=False)
    tipo = db.Column(db.Enum("base", "complemento", name="tipo_ingrediente"), nullable=False)
    sabor = db.Column(db.String(100), nullable=True)
    heladeria_id = db.Column(db.Integer, db.ForeignKey("heladeria.id")) 

    ingrediente_productos = relationship("Producto_Ingrediente", back_populates="ingrediente")
    heladeria = relationship("Heladeria", back_populates="ingredientes")


    def abastecer(self):
        if self.tipo == 'complemento':
            self.inventario += 10
            return True
        else:
            self.inventario += 5
            return  False


    def es_sano(self) -> bool:
        return esto_es_sano(self.calorias, self.es_vegetariano)
    
    def renovar_inventario(self, cantidad = 0) -> None:
        if self.tipo == 'complemento':
            self.inventario = cantidad
            return True
        else:
            raise ValueError (self.nombre)


    @classmethod
    def create_test_ingredientes(cls):
        if not cls.query.first():
            dummy_ingredients = [
                Ingrediente(id=1, nombre="Chocolate", precio=10.0, calorias=200, inventario=50, es_vegetariano=True, tipo="base", sabor="dulce", heladeria_id = 1 ),
                Ingrediente(id=2, nombre="Fresa", precio=12.0, calorias=150, inventario=40, es_vegetariano=True, tipo="base", sabor="frutal", heladeria_id = 1),
                Ingrediente(id=3, nombre="Vainilla", precio=11.0, calorias=180, inventario=45, es_vegetariano=True, tipo="base", sabor="dulce", heladeria_id = 1),
                Ingrediente(id=4, nombre="Mango", precio=14.0, calorias=160, inventario=35, es_vegetariano=True, tipo="base", sabor="frutal", heladeria_id = 1),
                Ingrediente(id=5, nombre="Café", precio=9.0, calorias=120, inventario=30, es_vegetariano=True, tipo="base", sabor="amargo", heladeria_id = 1),
                
                Ingrediente(id=6, nombre="Galleta", precio=5.0, calorias=180, inventario=30, es_vegetariano=True, tipo="complemento", heladeria_id = 1),
                Ingrediente(id=7, nombre="Caramelo", precio=8.0, calorias=220, inventario=25, es_vegetariano=False, tipo="complemento", heladeria_id = 1),
                Ingrediente(id=8, nombre="Almendras", precio=15.0, calorias=250, inventario=20, es_vegetariano=True, tipo="complemento", heladeria_id = 1),
                Ingrediente(id=9, nombre="Coco", precio=13.0, calorias=190, inventario=28, es_vegetariano=False, tipo="complemento", heladeria_id = 1),
                Ingrediente(id=10, nombre="Jarabe de Fresa", precio=7.0, calorias=200, inventario=40, es_vegetariano=True, tipo="complemento", heladeria_id = 1),
            ]

            db.session.bulk_save_objects(dummy_ingredients)
            db.session.commit()