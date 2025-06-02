'''problema eliminar repetidos (in s:seq⟨Char⟩) : seq⟨Char⟩ {
requiere: { T rue }
asegura: { (|res| ≤ |s|) ∧ (para todo i ∈ Z si 0 ≤ i < |s| → pertenece(s[i], res)) ∧ (para todo i, j ∈ Z si
(0 ≤ i, j < |res| ∧ i ̸= j) → res[i] ̸= res[j]) }
}'''
    

'''def cantidad_apariciones(elemento: str, lista: list[str]) -> int:
    apariciones: list[str] = []
    for indice in range(0,len(lista)):
        if lista[indice] == elemento:
            apariciones = apariciones + [elemento]
            
    return(len(apariciones))

def eliminar_repetidos(lista:list[str]) -> list[str]: 
    sin_repetidos: list[str] = []
    repetido: list[str] = []
    for elemento in lista:
        if cantidad_apariciones(elemento,lista) > 1 :
            repetido = [elemento]    
        else:
           sin_repetidos = sin_repetidos + [elemento]

    return sin_repetidos + repetido
print(eliminar_repetidos(['t','a','m','a','r','a']))'''


'''otra implementación más directa

'''

def eliminar_repetidos(lista:list[str]) -> list[str]:
    sin_repetidos: list[str] = []
    for elemento in lista:
        if elemento not in sin_repetidos:
            sin_repetidos.append(elemento)
    return sin_repetidos

print(eliminar_repetidos(['t','a','m','a','r','a']))