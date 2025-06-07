'''problema intercalar (in c1: Cola, in c2: Cola) : Cola {
requiere: {c1 y c2 tienen la misma cantidad de elementos}
asegura: {res solo contiene los elementos de c1 y c2}
asegura: {res contiene todos los elementos de c1 y c2, intercalados y respetando el orden original}
asegura: {El primer elemento de res es el primer elemento de c1}
asegura: {El tamaño de res es igual al doble del tamaño de c1}
'''
from queue import Queue as Cola

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

def intercalar(c1: Cola, c2: Cola) -> Cola:
    c1_copia: Cola = copiar_cola(c1)
    c2_copia: Cola = copiar_cola(c2)
    res: Cola = Cola()
    for elemento_c1 in c1:
        c1_copia.get(elemento_c1)
        res.put(elemento_c1)
        for elemento_c2 in c2:
            c2_copia.get(elemento_c2)
            res.put(elemento_c2)
        
    return res

    





    

    