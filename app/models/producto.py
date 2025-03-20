from sqlalchemy.orm import relationship
from app.config.db import db
from funciones import costos, las_calorías, rentabilidad

class Producto(db.Model):
    __tablename__ = "productos"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable= False)
    nombre  = db.Column(db.String(500), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    tipo_vaso = db.Column(db.String(100), nullable=True)
    volumen = db.Column(db.Float, nullable=True)
    tipo = db.Column(db.Enum("Copa", "Malteada", name="tipo_producto"), nullable=False)
    heladeria_id = db.Column(db.Integer, db.ForeignKey("heladeria.id"))

    producto_ingredientes = relationship("Producto_Ingrediente", back_populates="producto")
    heladeria = relationship("Heladeria", back_populates="productos")


    def obtener_ingredientes(self):
        return [pi.ingrediente for pi in self.producto_ingredientes]

    def calcular_costo(self):
        return costos(self) + 500

    def calcular_calorias(self) -> float:
        ingredientes = self.obtener_ingredientes()
        kcalorias_list = [ingrediente for ingrediente in ingredientes]
        return las_calorías(kcalorias_list) + 200

    def calcular_rentabilidad(self) -> float:
        return rentabilidad(self)



    @classmethod
    def create_test_products(cls):
        if not cls.query.first():
            dummy_products = [
                Producto(id = 1, nombre = 'Copa de fresa', precio=50.0, tipo="Copa", tipo_vaso="Vidrio", heladeria_id = 1),
                Producto(id = 2,nombre = 'Malteada deliciosa', precio=60.0, tipo="Malteada", volumen=300, heladeria_id = 1),
                Producto(id = 3,nombre = 'Chocoexplosion', precio=90.0, tipo="Copa", tipo_vaso="Vidrio", heladeria_id = 1),
                Producto(id = 4,nombre = 'Fresas crujientes', precio=60.0, tipo="Malteada", volumen=1300, heladeria_id = 1)
            ]
            db.session.bulk_save_objects(dummy_products)
            db.session.commit()