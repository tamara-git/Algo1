'''problema pos minimo (in s:seq⟨Z⟩) : Z {
requiere: { T rue }
asegura: { (Si |s| = 0, entonces res = −1; si no, res = al índice de la posición donde aparece el menor elemento
de s (si hay varios es la última aparición) }'''

def minimo(lista:list[int]) -> int:
    minimo: int = lista[0]
    for elemento in lista:
        if elemento <= minimo:
            minimo = elemento 
    return minimo

def pos_minimo(lista:list[int]) -> int:
    for indice in range (len(lista)):
        if len(lista) == 0:
            return -1
        else:
            if lista[indice] == minimo(lista):
                return indice