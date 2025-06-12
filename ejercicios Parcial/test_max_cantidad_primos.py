import unittest

from simulacro_parcial import maxima_cantidad_primos

class Test_maxima_cantidad_primos(unittest.TestCase):
    def test_matriz_3x3(self):

        self.assertEqual(maxima_cantidad_primos([[1,11,5],[0,2,10],[2,7,9]]),3)


if __name__ == "__main__":
    unittest.main(verbosity=2)