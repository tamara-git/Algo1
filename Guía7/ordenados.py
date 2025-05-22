'''problema ordenados (in s:seq⟨Z⟩) : Bool {
requiere: { True }
asegura: { res = true ↔(para todo i ∈ Z si 0 ≤ i < (|s| − 1) → s[i] < s[i + 1] }
}'''
def ordenados(lista:list[int]) -> bool:
    for indice in range(len(lista) - 1):
        if lista[indice] > lista[indice+1]:
            return False
    else:
        return True

print(ordenados([4,10,30,8]))
print(ordenados([4,10,30]))
print(ordenados([1,2,8,3,4]))