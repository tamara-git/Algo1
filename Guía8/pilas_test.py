import unittest
from queue import LifoQueue as Pila
from Pilas import buscar_nota_maxima, esta_bien_balanceada, pila_de_parentesis

class test_buscar_nota_maxima(unittest.TestCase):
    def test_dos_elementos(self):
        pila: Pila[int] = Pila()
        pila.put(("Math",7))
        pila.put(("E",5))
        res = ("Math",7)
        self.assertEqual(buscar_nota_maxima(pila), res)


if __name__ == '__main__':
    unittest.main(verbosity=2)