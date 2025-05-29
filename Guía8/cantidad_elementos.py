'''problema cantidad elementos (in p: Pila) : Z {
requiere: {True}
asegura: {res es igual a la cantidad de elementos que contiene p}
}
No se puede utilizar la función LifoQueue.qsize(). Tener en cuenta que, al usar get() para recorrer la pila, se modifica el
par´ametro de entrada, ya que los elementos se eliminan al accederse. Dado que la especificaci´on lo define como de tipo in, debe
restaurarse posteriormente.'''

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

#Hace la copia y restaura la original.
    while not pila_auxiliar.empty():
        elemento_desapilado: int = pila_auxiliar.get()
        pila_copiada.put(elemento_desapilado)
        pila.put(elemento_desapilado)
    return pila_copiada
  
def cantidad_elementos(pila:Pila[int]) -> int:
    pila_copiada: Pila[int] = copiar_pila(pila)
    cantidad: int = 0  
    while not pila_copiada.empty():
        pila_copiada.get()
        cantidad += 1
    return cantidad
    
   







