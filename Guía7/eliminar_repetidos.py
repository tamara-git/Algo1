'''problema eliminar repetidos (in s:seq⟨Char⟩) : seq⟨Char⟩ {
requiere: { T rue }
asegura: { (|res| ≤ |s|) ∧ (para todo i ∈ Z si 0 ≤ i < |s| → pertenece(s[i], res)) ∧ (para todo i, j ∈ Z si
(0 ≤ i, j < |res| ∧ i ̸= j) → res[i] ̸= res[j]) }
}'''
    
def eliminar_repetidos(lista:list[str]) -> list[str]:
   lista_nueva = lista.copy()
   for indice in range(len(lista)): 
    if lista_nueva[indice] not in 




print(eliminar_repetidos(['t','a','m','a','r','a']))
