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

    def test_True_2(self):
        pila_2 : Pila[str] = Pila(
        pila_2.put('1')
        pila_2.put('')
        pila_2.put('+')
        pila_2.put('')
        pila_2.put('(')
        pila_2.put('')
        pila_2.put('2')
        pila_2.put('')
        pila_2.put('*')
        pila_2.put('')
        pila_2.put('3')
        pila_2.put('')
        pila_2.put('=')
        pila_2.put('')
        pila_2.put('(')
        pila_2.put('')
        pila_2.put('2')
        pila_2.put('')
        pila_2.put('0')
        pila_2.put('')
        pila_2.put('/')
        pila_2.put('')
        pila_2.put('5')
        pila_2.put('')
        pila_2.put(')')
        pila_2.put('')
        pila_2.put(')')
        )
        #1 + ( 2 x 3 = ( 2 0 / 5 ) )

        self.assertTrue(esta_bien_balanceada(pila_2))


    def test_False(self):
        pila1: Pila[str] = Pila()
        pila1.put('5')
        pila1.put('*')
        pila1.put(')')
        pila1.put('3')
        pila1.put(')')
        pila1.put('*')
        pila1.put('(')      

        pila2: Pila[str] = Pila()
        pila2.put(')')
        pila2.put('*')
        pila2.put('(')
        pila2.put('3')
        pila2.put(')')
        pila2.put('*')
        pila2.put('(')    

        self.assertFalse(esta_bien_balanceada(pila1))  
        self.assertFalse(esta_bien_balanceada(pila2))


if __name__ == "__main__":
    unittest.main(verbosity=2)