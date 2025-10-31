import unittest
from parcial_2c2024 import palabras_por_vocales, mejor_resultado_de_ana
from queue import Queue as Cola

class Test_palabras_por_vocales(unittest.TestCase):
    def test_ejemplo(self):
        texto: str = "Mi perro Paco come albondigas"
        res: dict[int,int] = {1:1, 2:3, 4:1}
        self.assertEqual(palabras_por_vocales(texto), res)

    def test_ejemplo_2(self):
        texto: str = "Me gustan las matematicas"
        res: dict[int,int] = {1:2, 2:1, 5:1}
        self.assertEqual(palabras_por_vocales(texto), res)

class Test_mejor_resultado_de_ana(unittest.TestCase):
    def test_False_mayor_a_True_una_sola_lista(self):
        examenes: Cola[list[bool]] = Cola()
        examen: list[bool] = [False, True, False, False, False, True]
        examenes.put(examen)
        res: list[int] = [5]
        self.assertEqual(mejor_resultado_de_ana(examenes), res)
    
    def test_tres_listas(self):
        examenes: Cola[list[bool]] = Cola()
        examen1: list[bool] = [False, True, False, False, False, False]
        examen2: list[bool] = [True, True, False, False, False, True]
        examen3: list[bool] = [True, False, False, False, True, False]
        examenes.put(examen1)
        examenes.put(examen2)
        examenes.put(examen3)
        res: list[int] = [4,6,5]
        self.assertEqual(mejor_resultado_de_ana(examenes), res)


if __name__ == '__main__':
    unittest.main(verbosity=2)