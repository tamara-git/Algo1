import unittest

from promedio_de_salidas import calcular_promedio, promedio_de_salidas

class Test_promedio_de_salidas(unittest.TestCase):
    def test_tres_participante(self):
        registro: dict[str,list[int]] = {
            "carla": [30,40,60,61,60],
            "marta": [5,40,20],
            "julia": [10,38]
        }

        res: dict[str,tuple[int,float]] = {
            "carla": (3,(30 + 40 + 60)/3),
            "marta": (3,(5 + 40 + 20)/3),
            "julia": (2,(10 + 38)/2)
        }

        self.assertEqual(promedio_de_salidas(registro), res)

    def test__promedio_un_participante(self):
        lista: list[int] = [30,40,60,61,60]
        promedio: float = (30+40+60)/3

        self.assertAlmostEqual(calcular_promedio(lista), promedio)


if __name__ == "__main__":
    unittest.main(verbosity=2)