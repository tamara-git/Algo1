import unittest

from atencion_a_clientes import atencion_a_clientes, Cola, copiar_cola

def son_colas_iguales(c1: Cola[tuple[str, int, bool, bool]], c2: Cola[tuple[str, int, bool, bool]]) -> bool:
    c1_copia: Cola[tuple[str, int, bool, bool]] = copiar_cola(c1)
    c2_copia: Cola[tuple[str, int, bool, bool]] = copiar_cola(c2)
    lista_c1: list[tuple[str, int, bool, bool]] = []
    lista_c2: list[tuple[str, int, bool, bool]] = []

    while not c1_copia.empty():
        datos_c1: tuple[str, int, bool, bool] = c1_copia.get()
        lista_c1 = lista_c1.append(datos_c1)
        
    while not c2_copia.empty():
        datos_c2: tuple[str, int, bool, bool] = c2_copia.get()
        lista_c2 = lista_c2.append(datos_c2)

    
    for indice in range(len(lista_c1)):
        if lista_c1[indice] != lista_c2[indice] or len(lista_c1) != len(lista_c2):
            return False
    return True


class Test_atencion_a_clientes(unittest.TestCase):
    def con_una_prioridad(self):
        cola: Cola[tuple[str,int,bool,bool]] = Cola()
        cola.put(("Pablo",47344554,False,True))
        cola.put(("Brunilda", 94256891, False, True))
        cola.put(("Kiara", 10245697, True, False))
        cola.put(("Tamara", 46683766, False, False))

        cola_ordenada: Cola[tuple[str,int,bool,bool]] = Cola()
        cola_ordenada.put(("Kiara", 10245697, True, False))
        cola_ordenada.put(("Pablo", 47344554,False,True))
        cola_ordenada.put(("Brunilda", 94256891, False, True))
        cola_ordenada.put(("Tamara", 46683766, False, False))

        self.assertTrue(son_colas_iguales(atencion_a_clientes(cola), cola_ordenada))


if __name__ == "__main__":
    unittest.main(verbosity=2)