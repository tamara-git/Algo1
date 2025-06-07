import unittest, os

from existe_palabra import cadena_a_lista_palabras, existe_palabra


class Test_cadena_a_lista_palabras(unittest.TestCase):
    def test_cadena_hola_como_estas(self):
        self.assertEqual(cadena_a_lista_palabras("como estas\n"), ["como","estas"])


class Test_existe_palabra(unittest.TestCase):
    def test_dos_lineas(self):
        archivo = open("linea.txt", "r", encoding="utf-8")
        archivo.close()
        self.assertTrue(existe_palabra("linea.txt", "estas"))
        self.assertFalse(existe_palabra("linea.txt", "bien"))

if __name__ == "__main__":
    unittest.main(verbosity=2)
