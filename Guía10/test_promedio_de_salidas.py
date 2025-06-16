import unittest

from promedio_de_salidas import calcular_promedio

class Test_promedio_de_salidas(unittest.TestCase):
    def un_participante(self):
        registro: dict[str,list[int]] = {
            "carla": [30,40,60,61]
        }

        promedio: float = (30+40+60)/3
        self.assertAlmostEqual(calcular_promedio(registro), promedio)


if __name__ == "__main__":
    unittest.main(verbosity=2)