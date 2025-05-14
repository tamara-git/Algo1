#para importar todas las funciones de un archivo 
#from archivo import *

import unittest

from suma import suma

class Test_Suma(unittest.TestCase):

    def test_suma_positiva(self):
        self.assertEqual(suma(2,3),5)

    def test_suma_negativos(self):
        self.assertEqual(suma(-4,-2),-6)


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


from devolver_el_doble_si_es_par import devolver_el_doble_si_es_par
class test_devolver_el_doble_si_es_par(unittest.TestCase):
    def test_devolver_el_doble_cero_uno(self):
        self.assertEqual(devolver_el_doble_si_es_par(0),1)
        self.assertEqual(devolver_el_doble_si_es_par(),)
        self.assertEqual(devolver_el_doble_si_es_par(1),1)

    def test_devolver_el_doble_numero_par(self):
        self.assertEqual(devolver_el_doble_si_es_par((2),4))
        self.assertEqual(devolver_el_doble_si_es_par((10),20))

    def test_devolver_el_doble_numero_impar(self):
        self.assertEqual(devolver_el_doble_si_es_par((3),3))
        self.assertEqual(devolver_el_doble_si_es_par((11),11))

from farenheit_a_celcius import farenheit_a_celcius
class test_farenheit_a_celcius(unittest.TestCase):
    def test_1(self):
        self.assertAlmostEqual(farenheit_a_celcius((140.0),60.0))
        self.assertAlmostEqual(farenheit_a_celcius((140.0),60.5))
        
from es_primo import es_primo                              
class test_es_primo(unittest.TestCase):
    def test_uno_y_cero(self):
        self.assertFalse(es_primo(0))
        self.assertFalse(es_primo(1))

    def test_primo(self):
        self.assertTrue(es_primo(2))
        self.assertTrue(es_primo(17))

    def test_compuesto(self):
        self.assertTrue(es_primo(4))
        self.assertTrue(es_primo(964))

    def test_negativo(self):
        self.assertTrue(es_primo(-2))
        self.assertTrue(es_primo(-17))
        self.assertTrue(es_primo(-964))
        self.assertTrue(es_primo(-4))


if __name__ == '__main__':
    unittest.main(verbosity=2)