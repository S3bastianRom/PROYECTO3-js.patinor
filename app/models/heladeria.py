from sqlalchemy.orm import relationship
from app.config.db import db
from funciones import mejor_producto

class Heladeria(db.Model):
    __tablename__ = "heladeria"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    contador_ventas_dia = db.Column(db.Integer, default=0)
    total_ventas = db.Column(db.Float, default=0)

    ingredientes = relationship("Ingrediente", back_populates="heladeria")
    productos = relationship("Producto", back_populates="heladeria")


    def obtener_mejor_producto(self) -> str:
        return mejor_producto(*self.productos)


    def vender(self, nombre_producto: str) -> bool:
        producto = next((p for p in self.productos if p.nombre == nombre_producto), None)

        if not producto:
            return False

        for ingrediente in producto.obtener_ingredientes():
            cantidad_necesaria = 0.2 if ingrediente.tipo == "base" else 1

            if ingrediente.inventario < cantidad_necesaria:
                raise ValueError (ingrediente.nombre)

            ingrediente.inventario -= cantidad_necesaria

        self.total_ventas += producto.precio
        self.contador_ventas_dia += 1
        return "¡Vendido!"
    

    @classmethod
    def create_test_heladeria(cls):
        if not cls.query.first():
            dummy_heladeria = [
                Heladeria(id = 1, contador_ventas_dia = 0 , total_ventas = 0)
            ]
            db.session.bulk_save_objects(dummy_heladeria)
            db.session.commit()