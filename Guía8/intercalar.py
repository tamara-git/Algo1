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

    





    

    