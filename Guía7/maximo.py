''''. problema maximo (in s:seq⟨Z⟩) : Z {
requiere: { |s| > 0 }
asegura: { res = al mayor de todos los números que aparece en s }
}'''

def maximo(lista:list[int]) -> int:
    maximo : int = lista[0]
    for elemento in lista:
        if elemento >= maximo:   
            maximo = elemento
    return maximo
        
print(maximo([1,2,33,4,5,6]))