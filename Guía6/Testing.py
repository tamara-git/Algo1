import unittest

from suma import suma

class Test_Suma(unittest.TestCase):

    def test_suma_positiva(self):
        self.assertEqual(suma(2,3),5)

    def test_suma_negativos(self):
        self.assertEqual(suma(-4,-2),-6)
