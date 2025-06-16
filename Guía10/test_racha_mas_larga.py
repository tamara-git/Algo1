import unittest

from racha_mas_larga import racha_mas_larga

class Test_racha_mas_larga(unittest.TestCase):
    def test_una_racha_larga(self):
        tiempos: list[int] = [20,0,61,10,61,40,25,0,60,61,30,40,50,60,70]
        res: tuple[int,int] = (30,70)
        self.assertEqual(racha_mas_larga(tiempos), res)

if __name__ == "__main__":
    unittest.main(verbosity=2)