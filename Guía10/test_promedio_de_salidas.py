import unittest

from promedio_de_salidas import calcular_promedio, promedio_de_salidas

class Test_promedio_de_salidas(unittest.TestCase):
    def test_un_participante(self):
        registro: dict[str,list[int]] = {
            "carla": [30,40,60,61,60.3],
            "marta": [5,40.5,20.3],
            "julia": [10.5,38.20]
        }

        res: dict[str,tuple[int,float]] = {
            "carla": (3,(30 + 40 + 60)/3),
            "marta": (3,(5 + 40.5 + 20.3)/3),
            "julia": (2,(10.5 + 38.20)/2)
        }

        self.assertAlmostEqual(promedio_de_salidas(registro), res)

    def test__promedio_un_participante(self):
        registro: dict[str,list[int]] = {
            "carla": [30,40,60,61,60.3]
        }

        promedio: list[float] = [(30+40+60)/3]
        self.assertAlmostEqual(calcular_promedio(registro), promedio)


if __name__ == "__main__":
    unittest.main(verbosity=2)