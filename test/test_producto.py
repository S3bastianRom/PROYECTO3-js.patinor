import unittest
from app.models.ingrediente import Ingrediente
from app.models.producto_ingrediente import Producto_Ingrediente
from app.models.producto import Producto
from app.models.heladeria import Heladeria

class TestProductos(unittest.TestCase):
    def setUp(self):
        self.producto1 = Producto(id=1, nombre='Copa de fresa', precio=50.0, tipo="Copa", tipo_vaso="Vidrio", heladeria_id=1)
        self.producto2 = Producto(id=2, nombre='Malteada deliciosa', precio=60.0, tipo="Malteada", volumen=300, heladeria_id=1)

    def test_calcular_costo(self):
        costo = self.producto1.calcular_costo()
        self.assertIsInstance(costo, (int, float), "El costo debe ser un número")
        self.assertGreaterEqual(costo, 500, "El costo debe ser mayor a 500")

    def test_calcular_calorias(self):
        calorias = self.producto1.calcular_calorias()
        self.assertIsInstance(calorias, int, "Las calorías deben ser un número decimal")
        self.assertGreaterEqual(calorias, 200, "Las calorías deben ser mayores a 200")

    def test_calcular_rentabilidad(self):
        rentabilidad = self.producto1.calcular_rentabilidad()
        self.assertIsInstance(rentabilidad, float, "La rentabilidad debe ser un número decimal")
        self.assertGreaterEqual(rentabilidad, 0, "La rentabilidad no debe ser negativa")
