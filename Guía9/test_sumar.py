import unittest

from sumar import sumar

class Test_sumar(unittest.TestCase):
    def test_y_positivo(self):
        resultado_obtenido = sumar(2,2)
        resultado_esperado = 4
        self.assertEqual(resultado_obtenido,resultado_esperado)

    def test_y_negativo(self):
        resultado_obtenido = sumar(2,-2)
        resultado_esperado = 0
        self.assertEqual(resultado_obtenido,resultado_esperado)

if __name__ == "__main__":
    unittest.main(verbosity=2)

'''pip install coverage'''
#para correr los test, en terminal, cada vez que modifico el test, vuelvo a hacer el coverage run
'''coverage run --include=sumar.py -m  unittest test_sumar.py
    coverage run --omit=test_sumar.py'''  #probar con comillas o sin comillas el "test_sumar.py" o test_* omite todos de este tipo

#branches son las aristas del true/false en if, for y while

#95% para lineas y branches
#(branch -BrPart/ branch) * 100%

#(lineas_totales-lineas_que_no_corrieron/ lineas_totales) * 100%