import unittest

from calcular_valor_inventario import calcular_valor_inventario

class Test_valor_inventario(unittest.TestCase):
    def test_dos_productos(self):
        inventario: dict[str, dict[str, float | int]] = {
            "Camisa": {"precio":20.0, "cantidad": 10},
            "Pantalón": {"precio": 30.0, "cantidad": 30}
        }

        calcular_valor_inventario(inventario)

if __name__ == "__main__":
    unittest.main(verbosity=2)