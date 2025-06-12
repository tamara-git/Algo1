import unittest

from actualizar_stock import actualizar_stock

class Test_actualizar_stock(unittest.TestCase):
    def test_un_producto(self):
        inventario: dict[str, dict[str, float | int]] = {
            "remera": {"precio": 10000, "cantidad": 6} 
        }

        actualizar_stock(inventario, "remera", 4)

if __name__ == "__main__":
    unittest.main(verbosity=2)