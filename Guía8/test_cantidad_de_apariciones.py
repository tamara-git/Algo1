import unittest
from cantidad_de_apariciones import cantidad_de_apariciones

class Test_cantidad_de_apariciones(unittest.TestCase):
    def test_2_apariciones(self):
        archivo = open("archivo.txt", "r", encoding= "utf-8")
        archivo.write("hermosa mañana verdad\ndemasiada hermosa para ser verdad")
        archivo.close()

        self.assertEqual(cantidad_de_apariciones("archivo.txt","hermosa"), 2)

    def test_1_aparicion(self):
        archivo_2 = open("otro_archivo.txt", "r", encoding= "utf-8")
        archivo_2.write("hermosa mañana verdad\ndemasiado para ser cierto")
        archivo_2.close()

        self.assertEqual(cantidad_de_apariciones("otro_archivo.txt","hermosa"), 1)