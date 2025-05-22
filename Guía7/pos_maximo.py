'''problema pos maximo (in s:seq⟨Z⟩) : Z {
requiere: { T rue }
asegura: { (Si |s| = 0, entonces res = −1; si no, res = al índice de la posición donde aparece el mayor elemento
de s (si hay varios es la primera aparici´on) }
}
'''
def maximo(lista:list[int]) -> int:
    maximo : int = lista[0]
    for elemento in lista:
        if elemento >= maximo:   
            maximo = elemento
    return maximo

def pos_maximo(lista:list[int]) -> int:
    for indice in range(len(lista)):
        if len(lista) == 0:
            return -1
        else:
            if lista[indice] == maximo(lista):
                return indice
        
print(pos_maximo([1,2,33,4,5,6]))