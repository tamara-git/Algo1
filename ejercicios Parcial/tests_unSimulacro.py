import unittest
from un_simulacro import convertir_a_diccionario, ultima_aparicion, elementos_exclusivos, contar_traducciones_iguales

class Test_Convertir_A_Diccionario(unittest.TestCase):
    def test_dado(self):
        lista = [-1,0,4,100,100,-1,-1]
        res = {100: 2, -1:3, 0:1, 4:1}
        self.assertEqual(convertir_a_diccionario(lista), res)

    # def test_propio(self):
    #     lista = [-1,0,4,100,100,-1,-1]
    #     res = {-1:3, 0:1, 4:1, 100:2}
    #     self.assertEqual(convertir_a_diccionario(lista), res)

class Test_ultima_aparicion(unittest.TestCase):
    def test_parcial(self):
        lista = [8,2,3,4,5,6,7,8,8]
        self.assertEqual(ultima_aparicion(lista, 4), 3)

class Test_Elementos_Exclusivos(unittest.TestCase):
    def test_propio(self):
        lista1 = [1,2,3,4,6,2,53]
        lista2 = [5,2,3,8,70,99,45,3,2]
        res = [1,4,6,53,5,8,70,99,45]
        self.assertEqual(elementos_exclusivos(lista1,lista2), res)


class Test_Contar_Traducciones_Iguales(unittest.TestCase):
    def test_ejemplo(self):
        aleman = {"Mano": "Hand", "Pie": "Fuss", "Dedo": "Finger", "Cara": "Gesicht"}
        inglés = {"Pie": "Foot", "Dedo": "Finger", "Mano": "Hand"}
        res = 2
        self.assertEqual(contar_traducciones_iguales(inglés, aleman), res)
if __name__ == '__main__':
    unittest.main(verbosity=2)