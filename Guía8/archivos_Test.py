import unittest
from typing import TextIO
from archivos import contar_lineas

class Test_contar_lineas(unittest.TestCase):
    def test_contar_lineas_archivo_vacio(self):
        ruta_archivo: str = os.path.join("archivos_test","archivo_con_una_linea_vacia.txt")
        resultado = contar_lineas(ruta_archivo)
        self.assertEqual(resultado, 1)


if __name__ == '__main__':
    unittest.main(verbosity=2)