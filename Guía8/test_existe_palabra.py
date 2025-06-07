import unittest

from existe_palabra import existe_palabra, TextIO

class Test_existe_palabra(unittest.TestCase):
    def test_una_linea(self):
        archivo: TextIO = open("linea.txt", "r", encoding = "utf-8")
        
        self.assertTrue(existe_palabra(archivo, "verano"))
        self.assertFalse(existe_palabra(archivo, "invierno"))

        archivo.close()


