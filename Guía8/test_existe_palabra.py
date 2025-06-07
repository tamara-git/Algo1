import unittest, os

from existe_palabra import cadena_a_lista_palabras, existe_palabra

class Test_existe_palabra(unittest.TestCase):
    def test_dos_lineas(self):
        archivo = open("lineas.txt", "w", encoding = "utf-8")
        archivo.write("como estas\nyo soy tamara")
        archivo.close()

        self.assertTrue(existe_palabra("lineas.txt", "estas"))
        self.assertFalse(existe_palabra("lineas.txt", "bien"))

    def test_tres_lineas(self):
        archivo = open("texto.txt", "w", encoding = "utf-8")
        archivo.write("como estas\n todo bien\nsoy tamara")
        archivo.close()

        self.assertTrue(existe_palabra("texto.txt", "bien"))
        self.assertFalse(existe_palabra("texto.txt", "mal"))


    def test_cadena_hola_como_estas(self):
        self.assertEqual(cadena_a_lista_palabras("como estas\n"), ["como","estas"])

if __name__ == "__main__":
    unittest.main(verbosity=2)
