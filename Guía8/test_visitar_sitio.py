import unittest

from visitar_sitio import visitar_sitio
from queue import LifoQueue as Pila

class Test_visitar_sitio(unittest.TestCase):
    def test_un_usuario(self):

        historiales_inicio: dict[str,Pila[str]] = {}

        historial_kiara: Pila[str] = Pila()
        historial_kiara.put("pinterest.com")
    
        historiales: dict[str,Pila[str]] = {
            "Kiara": historial_kiara
        }

        self.assertEqual(visitar_sitio(historiales_inicio, "Kiara", "pinterest.com"), historiales)

if __name__ == "__main__":
    unittest.main(verbosity=2)