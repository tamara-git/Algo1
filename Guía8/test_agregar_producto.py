import unittest

from agregar_producto import agregar_producto

class Test_agregar_producto(unittest.TestCase):
    def test_dos_productos(self):
        inventario_True: dict[str, dict[float | int]] = {
            "Medias Can Can": {"precio": 1999.99, "cantidad":4}
        }
        
        inventario_test: dict[str, dict[float | int]] = {}

        self.assertEqual(agregar_producto(inventario_test,"Medias Can Can", 1999.99, 4), inventario_True)


if __name__ == "__main__":
    unittest.main(verbosity=2)