import unittest
from dict import calcular_promedio_por_estudiante, calcular_valor_inventario

class test_calcular_promedio_por_estudiante(unittest.TestCase):
    def test_ejemplo(self):
        res: dict[str,float] = {"Sole": 9.25, "Maxi": 8.0}
        notas: list[tuple[str, float]] = [("Sole", 9.5), ("Maxi", 8.0), ("Sole", 9.0)]
        self.assertEqual(calcular_promedio_por_estudiante(notas),res)

    def test_un_estudiante(self):
        notas: list[tuple[str, float]] = [("Maxi", 8.0)]
        res: dict[str,float] = {"Maxi": 8.0}
        self.assertEqual(calcular_promedio_por_estudiante(notas),res)

class test_calcular_valor_inventario(unittest.TestCase):
    def test_ejemplo(self):
        inventario: dict[str, dict[str,int|float]] = {"remera": {"precio": 50, "cantidad": 2},
                                                      "pantalon": {"precio": 10, "cantidad": 4},
                                                      "short": {"precio": 20, "cantidad": 3}
                                                      }
        res: float = 200
        self.assertEqual(calcular_valor_inventario(inventario), res)

    def test_ejemplo_2(self):
        inventario: dict[str, dict[str,int|float]] = {"remera": {"precio": 10, "cantidad": 2},
                                                      "pantalon": {"precio": 10, "cantidad": 4},
                                                      "short": {"precio": 10, "cantidad": 3}
                                                      }
        res: float = 90
        self.assertEqual(calcular_valor_inventario(inventario), res)

if __name__ == '__main__':
    unittest.main(verbosity=2)