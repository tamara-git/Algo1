import unittest

from buscar_nota_maxima import buscar_nota_maxima, Pila

class Test_buscar_nota(unittest.TestCase):
    
    def test_nota_maxima_correcta(self):
        pila: Pila[tuple[str,int]] = Pila()
        pila.put(("pablo",6))
        pila.put(("kiara",10))

        self.assertEqual(buscar_nota_maxima(pila),("kiara",10))

    def test_nota_maxima_incorrecta(self):
        pila: Pila[tuple[str,int]] = Pila()
        pila.put(("pablo",10))
        pila.put(("kiara",6))

        self.assertNotEqual(buscar_nota_maxima(pila),("kiara",6))

if __name__ == "__main__":
    unittest.main(verbosity=2)