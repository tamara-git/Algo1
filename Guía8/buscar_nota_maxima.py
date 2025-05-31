'''Ejercicio 4. Implementar una solución para el siguiente problema.
problema buscar nota maxima (in p: Pila[seq⟨Char⟩×Z]) : seq⟨Char⟩ ×Z {
requiere: {p no está vacía}
requiere: {los elementos de p no tienen valores repetidos en la segunda posici´on de las tuplas}
asegura: {res es una tupla de p}
asegura: {No hay ningún elemento en p cuya segunda componente sea mayor que la segunda componente de res }
}'''

'''p = Pila () # crea una pila
p.put (1) # apila un 1
elemento = p.get () # desapila
p.empty () # devuelve true si y solo si la pila está vacía'''

from queue import LifoQueue as Pila

#primero hago una función que me cree una copia de la pila
def copiar_pila(pila:Pila[tuple[str,int]]) -> Pila[tuple[str,int]]:
    pila_auxiliar: Pila[tuple[str,int]] = Pila()
    pila_copia:  Pila[tuple[str,int]] = Pila()

#invierto la pila
    while not pila.empty():
        tupla: tuple[str,int] = pila.get()
        pila_auxiliar.put(tupla)

#hago la copia y restauro la pila
    while not pila_auxiliar.empty():
        tupla: tuple[str,int] = pila_auxiliar.get()
        pila_copia.put(tupla)
        pila.put(tupla)

    return pila_copia



def buscar_nota_maxima(pila:Pila[tuple[str,int]]) -> tuple[str,int]:
    pila_copia: Pila[tuple[str,int]] = copiar_pila(pila)
    # Notar que nota_maxima es una tupla = (estudiante,calificación), yo quiero acceder a la calificación.
    nota_maxima: tuple[str,int] = pila_copia.get()
    calificacion_maxima: int = nota_maxima[1]


    while not pila_copia.empty():
        tupla_actual: tuple[str,int] = pila_copia.get()
        if tupla_actual[1] > calificacion_maxima:
            calificacion_maxima = tupla_actual[1] 
            nota_maxima = tupla_actual

    return nota_maxima





