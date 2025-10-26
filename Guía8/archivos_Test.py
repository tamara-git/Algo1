import unittest
import os
from archivos import contar_lineas, clonar_sin_comentario, existe_palabra, cantidad_de_apariciones, invertir_lineas

class Test_contar_lineas(unittest.TestCase):
    def test_contar_lineas_archivo_vacio(self):
        ruta_archivo: str = os.path.join("archivos_test","archivo_con_una_linea_vacia.txt")
        resultado: int = contar_lineas(ruta_archivo)
        self.assertEqual(resultado, 1)

    def test_contar_lineas_archivo_con_10_lineas(self):
        ruta_archivo: str = os.path.join("archivos_test","archivo_con_10_lineas.txt")
        resultado: int = contar_lineas(ruta_archivo)
        self.assertEqual(resultado, 10)

 
class Test_clonar_sin_comentario(unittest.TestCase):
    def test_archivo_con_comentarios(self):
        ruta_archivo: str = os.path.join("archivos_test","archivo_con_comentarios.txt")
        archivo_de_salida: str = os.path.join("archivos_test","archivo_salida.txt")
        clonar_sin_comentario(ruta_archivo,archivo_de_salida)
        self.assertNotEqual(clonar_sin_comentario(ruta_archivo, archivo_de_salida), archivo_de_salida)
        self.assertNotEqual(contar_lineas(archivo_de_salida), contar_lineas(ruta_archivo))

class Test_existe_palabra(unittest.TestCase):
    def test_existe_palabra(self):
        ruta_archivo: str = os.path.join("archivos_test","archivo_existe_palabra.txt")
        res: bool = True
        esperado: bool = existe_palabra(ruta_archivo, "hola")
        self.assertEqual(esperado,res)

class Test_cantidad_de_apariciones(unittest.TestCase):
    def test_con_10_apariciones(self):
        ruta_archivo: str = os.path.join("archivos_test","archivo_10_apariciones.txt")
        resultado: int = cantidad_de_apariciones(ruta_archivo, "dia")
        self.assertEqual(resultado,10)

    def test_sin_apariciones(self):
        ruta_archivo: str = os.path.join("archivos_test","archivo_sin_apariciones.txt")
        resultado: int = cantidad_de_apariciones(ruta_archivo, "dia")
        self.assertEqual(resultado,0)


class Test_invertir_lineas(unittest.TestCase):
    def test_ejemplo(self):
        archivo_entrada: str = os.path.join("archivos_test","archivo_a_invertir.txt")
        archivo_salida: str = os.path.join("archivos_test","archivo_invertido.txt")
        resultado: str = invertir_lineas(archivo_entrada,archivo_salida)
        self.assertEqual(contar_lineas(archivo_salida),contar_lineas(archivo_entrada))
    






if __name__ == '__main__':
    unittest.main(verbosity=2)