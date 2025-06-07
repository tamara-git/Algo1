import unittest

from existe_palabra import cadena_a_lista_palabras, existe_palabra


class Test_cadena_a_lista_palabras(unittest.TestCase):
    def test_cadena_hola_como_estas(self):
        self.assertEqual(cadena_a_lista_palabras("como estas\nyo soy tamara"), ["como","estas"," yo", "soy", "tamara"])


class Test_existe_palabra(unittest.TestCase):
    def test_una_linea(self):
        self.assertTrue(existe_palabra("linea.txt", "verano"))
        self.assertFalse(existe_palabra("linea.txt", "invierno"))

if __name__ == "__main__":
    unittest.main(verbosity=2)
