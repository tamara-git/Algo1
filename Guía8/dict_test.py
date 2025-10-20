import unittest
from dict import calcular_promedio_por_estudiante

class test_calcular_promedio_por_estudiante(unittest.TestCase):
    def test_ejemplo(self):
        res: dict[str,float] = {"Sole": 9.25, "Maxi": 8.0}
        notas: list[tuple[str, float]] = [("Sole", 9.5), ("Maxi", 8.0), ("Sole", 9.0)]
        self.assertEqual(calcular_promedio_por_estudiante(notas),res)

    def test_un_estudiante(self):
        notas: list[tuple[str, float]] = [("Maxi", 8.0)]
        res: dict[str,float] = {"Maxi": 8.0}
        self.assertEqual(calcular_promedio_por_estudiante(notas),res)



if __name__ == '__main__':
    unittest.main(verbosity=2)