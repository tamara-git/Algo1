import unittest

from nivel_de_ocupacion import nivel_de_ocupacion

class Test_nivel_de_ocupacion(unittest.TestCase):
    def test_ejemplo(self):
        camas_por_piso: list[list[bool]] = [[False, True, False], [True, True, True], [True, True, False]]
        res: list[float] = [1/3, 3/3, 2/3]

        self.assertEqual(res, nivel_de_ocupacion(camas_por_piso))
