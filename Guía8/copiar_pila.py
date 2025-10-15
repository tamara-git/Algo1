from queue import LifoQueue as Pila

def copiar_pila(p: Pila[int]) -> [int]:
    pila_aux: Pila[int] = Pila()
    pila_copia: Pila[int] = Pila()
    while not p.empty():
        elemento: int = p.get()
        pila_aux.put(elemento)

    while not pila_aux.empty():
        elemento: int = pila_aux.get()
        p.put(elemento)
        pila_copia.put(elemento)
    return pila_copia