''''. problema maximo (in s:seq⟨Z⟩) : Z {
requiere: { |s| > 0 }
asegura: { res = al mayor de todos los números que aparece en s }
}'''

def maximo(lista:list[int]) -> int:
    for indice in range(len(lista)):
        if indice >= lista[indice]:
            return indice
        else:
            lista[indice]

def maximo(lista:list[int]) -> int:
    maximo : int = lista[0]
    for elemento in lista:
        if elemento >= maximo:   
            maximo = elemento
    return elemento
        
print(maximo([1,2,33,4,5,6]))