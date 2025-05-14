import unittest

from suma import suma

class Test_Suma(unittest.TestCase):

    def test_suma_positiva(self):
        self.assertEqual(suma(2,3),5)

    def test_suma_negativos(self):
        self.assertEqual(suma(-4,-2),-6)


if __name__ == '__main__':
    unittest.main(verbosity=2)


from es_multiplo_de import es_multiplo_de

class test_es_multiplo_de(unittest.TestCase):
    def test_es_multiplo_cero_y_uno(self):
        self.assertTrue(es_multiplo_de(0,5))
        self.assertFalse(es_multiplo_de(1,5))
        self.assertTrue(es_multiplo_de (15,1))

    def test_es_multiplo_valores_iguales(self):
        self.assertTrue(es_multiplo_de(8,8))
        self.assertEqual(es_multiplo_de(12,12),True)
        
    def test_es_multiplo_valores_distintos(self):
        self.assertTrue(es_multiplo_de(8,2))
        self.assertFalse(es_multiplo_de(3,2))