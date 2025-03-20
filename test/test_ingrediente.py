import unittest
from app.models.ingrediente import Ingrediente
from app.models.producto_ingrediente import Producto_Ingrediente
from app.models.producto import Producto
from app.models.heladeria import Heladeria

class TestIngredientes(unittest.TestCase):
    ig1 = Ingrediente(id=1, nombre="Chocolate", precio=10.0, calorias=200, inventario=50, es_vegetariano=True, tipo="base", sabor="dulce", heladeria_id = 1 )
    ig2 = Ingrediente(id=2, nombre="Fresa", precio=12.0, calorias=150, inventario=40, es_vegetariano=False, tipo="base", sabor="frutal", heladeria_id = 1)
    ig3 = Ingrediente(id=6, nombre="Galleta", precio=5.0, calorias=180, inventario=30, es_vegetariano=True, tipo="complemento", heladeria_id = 1)
    ig4 = Ingrediente(id=7, nombre="Caramelo", precio=8.0, calorias=220, inventario=25, es_vegetariano=False, tipo="complemento", heladeria_id = 1)

    
    def test_es_sano_true(self):
        self.assertTrue(self.ig1.es_sano())
    
    def test_es_sano_exception(self):
        with self.assertRaises(ValueError):
            self.ig2.es_sano()

    def test_abastecer(self):
        self.ig3.abastecer()
        self.assertEqual(self.ig3.inventario, 40)
        self.assertTrue(self.ig3.abastecer())
    
    def test_renovar_inventario(self):
        self.assertTrue(self.ig3.renovar_inventario())
        with self.assertRaises(ValueError) as context:
            self.ig1.renovar_inventario()
        
        self.assertEqual(str(context.exception), "Chocolate") 