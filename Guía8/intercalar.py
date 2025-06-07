'''problema intercalar (in c1: Cola, in c2: Cola) : Cola {
requiere: {c1 y c2 tienen la misma cantidad de elementos}
asegura: {res solo contiene los elementos de c1 y c2}
asegura: {res contiene todos los elementos de c1 y c2, intercalados y respetando el orden original}
asegura: {El primer elemento de res es el primer elemento de c1}
asegura: {El tamaño de res es igual al doble del tamaño de c1}
'''
from queue import Queue as Cola

def copiar_cola(cola: Cola) -> Cola:
    cola_auxiliar: Cola = Cola()
    cola_copia: Cola = Cola()

    # Desencolo los elementos e invierto el orden en cola_auxiliar.
    while len(cola) != 0:
        elemento = cola.get()
        cola_auxiliar.put(elemento)

    # Hago la copia y restauro la cola.
    while len(cola_auxiliar) != 0:
        elemento = cola_auxiliar.get()
        cola_copia.put(elemento)
        cola.put(elemento)

    return cola_copia


def intercalar(c1: Cola, c2: Cola) -> Cola:
    c1_copia: Cola = copiar_cola(c1)
    c2_copia: Cola = copiar_cola(c2)
    res: Cola = Cola()
    for elemento in c1, c2:
        c1_copia.get(elemento)
        res.put(elemento)
        c2_copia.get(elemento)
        res.put(elemento)
        
    return res

    





    

    