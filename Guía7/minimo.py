'''problema minimo (in s:seq⟨Z⟩) : Z {
requiere: { |s| > 0 }
asegura: { res = al menor de todos los n´umeros que aparece en s }
}'''

def minimo(lista:list[int]) -> int:
    minimo: int = lista[0]
    for elemento in lista:
        if elemento <= minimo:
            minimo = elemento 
    return minimo

print(minimo([5,77,5,26,1]))