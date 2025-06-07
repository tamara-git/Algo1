import unittest

from intercalar import intercalar, Cola

def copiar_cola(cola: Cola) -> Cola:
        cola_copia: Cola = Cola()

        # Desencolo los elementos, hago la copia y restauro la cola
        while not cola.empty():
            elemento = cola.get()
            cola_copia.put(elemento)
            cola.put(elemento)

        return cola_copia

def mismos_elementos(c1: Cola, c2: Cola) -> bool:
        lista_c1: list = []
        lista_c2: list = []
        c1_copia: Cola = copiar_cola(c1)
        c2_copia: Cola = copiar_cola(c2)
        
        while not c1_copia.empty():
            elemento_c1 = c1_copia.get()
            lista_c1.append(elemento_c1)
             
        while not c2_copia.empty():
            elemento_c2 = c2_copia.get()
            lista_c2.append(elemento_c2)

        for elemento1 in lista_c1:
            for elemento2 in lista_c2:
                if elemento1 == elemento2:
                    return True
                return False
            
def misma_longitud(c1: Cola, c2: Cola) -> bool:
        lista_c1: list = []
        lista_c2: list = []
        c1_copia: Cola = copiar_cola(c1)
        c2_copia: Cola = copiar_cola(c2)
        
        while not c1_copia.empty():
            elemento_c1 = c1_copia.get()
            lista_c1.append(elemento_c1)
             
        while not c2_copia.empty():
            elemento_c2 = c2_copia.get()
            lista_c2.append(elemento_c2)

        if len(lista_c1) == len(lista_c2):
            return True
        return False 

def son_colas_iguales(c1: Cola, c2: Cola) -> bool:
    if mismos_elementos(c1,c2) == True and misma_longitud(c1,c2) == True:
        return True
    return False

class Test_intercalar(unittest.TestCase):
    def test_cola_corta(self):

        c1: Cola = Cola()
        c1.put(1)
        c1.put(2)
        c1.put(10)

        c2: Cola = Cola()
        c2.put(20)
        c2.put(30)
        c2.put(15)

        res: Cola = Cola()
        res.put(1)
        res.put(20)
        res.put(2)
        res.put(30)
        res.put(10)
        res.put(15)

        self.assertTrue(son_colas_iguales(intercalar(c1,c2), res))

if __name__ == "__main__":
    unittest.main(verbosity=2)