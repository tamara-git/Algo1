'''Ejercicio 3. Implementar una soluci´on para el siguiente problema.
problema buscar el maximo (in p: Pila[Z]) : Z {
requiere: {p no est´a vac´ıa}
asegura: {res es un elemento de p}
asegura: {res es mayor o igual a todos los elementos de p}'''

'''p = Pila () # crea una pila
p.put (1) # apila un 1
elemento = p.get () # desapila
p.empty () # devuelve true si y solo si la pila está vacía'''

from queue import LifoQueue as Pila

def copiar_pila(pila:Pila[int]) -> Pila[int]:
    pila_auxiliar: Pila[int] = Pila()
    pila_copiada: Pila[int] = Pila()

#invierto la pila
    while not pila.empty():
        elemento_desapilado: int = pila.get()
        pila_auxiliar.put(elemento_desapilado)

#hago la copia y restauro la pila
    while not pila_auxiliar.empty():
        elemento_desapilado: int = pila_auxiliar.get()
        pila_copiada.put(elemento_desapilado)
        pila.put(elemento_desapilado)
    
    return pila_copiada


def buscar_el_maximo(pila:Pila[int]) -> int:
    pila_copiada: Pila[int] = copiar_pila(pila)
    #desapilo el ultimo elemento, y lo llamo máximo (porque no hay ningún elemento mayor a este, por el momento)
    máximo: int = pila_copiada.get() 

    #desapilo cada uno de los elementos, y lo comparo con el primer elemento desapilado.
    while not pila_copiada.empty():
        elemento_actual: int = pila_copiada.get()
        if elemento_actual > maximo:
            maximo = elemento_actual

    return maximo

    
        