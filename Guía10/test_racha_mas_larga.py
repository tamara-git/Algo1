import unittest

from racha_mas_larga import racha_mas_larga

class Test_racha_mas_larga(unittest.TestCase):
    def test_una_racha_larga(self):
        tiempos: list[int] = [30,40,50,60,70]
        res: tuple[int,int] = (0,4)
        self.assertEqual(racha_mas_larga(tiempos), res)

    def test_una_racha_larga_con_61(self):
        tiempos: list[int] = [30,61,40,50,60,70]
        res: tuple[int,int] = (2,5)
        self.assertEqual(racha_mas_larga(tiempos), res)
if __name__ == "__main__":
    unittest.main(verbosity=2)