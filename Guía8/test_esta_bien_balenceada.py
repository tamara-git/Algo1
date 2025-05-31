import unittest

from esta_bien_balanceada import esta_bien_balanceada, Pila

class Test_esta_bien_balanceada(unittest.TestCase):
  
    def test_True(self):
        pila: Pila[str] = Pila()
        pila.put('(')
        pila.put('5')
        pila.put('+')
        pila.put('3')
        pila.put(')')
        pila.put('*')
        pila.put('2')

        self.assertTrue(esta_bien_balanceada(pila))

    def test_False(self):
        pila: Pila[str] = Pila()
        pila.put('5')
        pila.put('*')
        pila.put(')')
        pila.put('3')
        pila.put(')')
        pila.put('*')
        pila.put('(')      

        self.assertFalse(esta_bien_balanceada(pila))  

if __name__ == "__main__":
    unittest.main(verbosity=2)