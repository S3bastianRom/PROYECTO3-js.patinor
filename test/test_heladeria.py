import unittest
from app.models.ingrediente import Ingrediente
from app.models.producto_ingrediente import Producto_Ingrediente
from app.models.producto import Producto
from app.models.heladeria import Heladeria

import unittest

class TestHeladeria(unittest.TestCase):
    ig1 = Ingrediente(id=1, nombre="Chocolate", precio=10.0, calorias=100, inventario=0, es_vegetariano=True, tipo="base", sabor="dulce", heladeria_id = 1 )
    ig2 = Ingrediente(id=2, nombre="Fresa", precio=12.0, calorias=150, inventario=40, es_vegetariano=False, tipo="base", sabor="frutal", heladeria_id = 1)
    ig3 = Ingrediente(id=6, nombre="Galleta", precio=5.0, calorias=180, inventario=30, es_vegetariano=True, tipo="complemento", heladeria_id = 1)
    ig4 = Ingrediente(id=7, nombre="Caramelo", precio=8.0, calorias=220, inventario=25, es_vegetariano=False, tipo="complemento", heladeria_id = 1)

    produdcto1 = Producto(id = 1, nombre = 'Copa de fresa', precio=50.0, tipo="Copa", tipo_vaso="Vidrio", heladeria_id = 1)
    produdcto2 = Producto(id = 2,nombre = 'Malteada deliciosa', precio=60.0, tipo="Malteada", volumen=300, heladeria_id = 1)
    produdcto3 = Producto(id = 3,nombre = 'Chocoexplosion', precio=90.0, tipo="Copa", tipo_vaso="Vidrio", heladeria_id = 1)
    produdcto4 = Producto(id = 4,nombre = 'Fresas crujientes', precio=60.0, tipo="Malteada", volumen=1300, heladeria_id = 1)
    
    re1 = Producto_Ingrediente(id = 1 , producto_id = 1 , ingrediente_id = 2)
    re2 =Producto_Ingrediente(id = 2 , producto_id = 1 , ingrediente_id = 6)
    re3 =Producto_Ingrediente(id = 3 , producto_id = 1 , ingrediente_id = 10)
    re4 =Producto_Ingrediente(id = 4 , producto_id = 2 , ingrediente_id = 3)
    re5 =Producto_Ingrediente(id = 5 , producto_id = 2 , ingrediente_id = 4)
    re6 =Producto_Ingrediente(id = 6 , producto_id = 3 , ingrediente_id = 5)
    re7 =Producto_Ingrediente(id = 7 , producto_id = 3 , ingrediente_id = 1)

    def setUp(self):
        self.heladeria = Heladeria()
        self.heladeria.productos = [
            self.produdcto1,
            self.produdcto2,
            self.produdcto3,
            self.produdcto4
        ]
        self.heladeria.total_ventas = 0
        self.heladeria.contador_ventas_dia = 0

    def test_obtener_mejor_producto(self):
        mejor_producto = self.heladeria.obtener_mejor_producto()
        self.assertIsInstance(mejor_producto, str)
        self.assertIn(mejor_producto, [p.nombre for p in self.heladeria.productos])

    def test_vender_producto_existente(self):
        resultado = self.heladeria.vender("Copa de fresa")
        self.assertEqual(resultado, "¡Vendido!")
        self.assertGreater(self.heladeria.total_ventas, 0)
        self.assertGreater(self.heladeria.contador_ventas_dia, 0)
    
    def test_vender_producto_inexistente(self):
        resultado = self.heladeria.vender("Helado mágico")
        self.assertFalse(resultado)