import unittest
from queue import LifoQueue as Pila
from Pilas import buscar_nota_maxima, esta_bien_balanceada, intercalar_testeo

class test_buscar_nota_maxima(unittest.TestCase):
    def test_dos_elementos(self):
        pila: Pila[int] = Pila()
        pila.put(("Math",7))
        pila.put(("E",5))
        res = ("Math",7)
        self.assertEqual(buscar_nota_maxima(pila), res)

class test_esta_bien_balanceada(unittest.TestCase):
    def test_ejemplo(self):
        s: str = "1 + ( 2 x 3 = ( 20 / 5 ) )"
        res: bool = True
        self.assertEqual(esta_bien_balanceada(s), res)

class test_intercalar(unittest.TestCase):
    def test_ejemplo(self):
        p1: Pila = Pila()
        p2: Pila = Pila()
        p1.put(1)
        p1.put(2)
        p2.put(3)
        p2.put(4)
        lista: list = [1,3,2,4]
        self.assertEqual(intercalar_testeo(p1,p2), lista)

    

if __name__ == '__main__':
    unittest.main(verbosity=2)