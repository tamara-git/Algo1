'''Recorrer una seq⟨Z⟩ y devolver verdadero si hay 3 números iguales consecutivos, en cualquier posición y 
False en caso contrario.
problema iguales consecutivos (in s:seq⟨Z⟩) : Bool {
requiere: { T rue }
asegura: { (res = true) ↔ (existe i, j, k ∈ Z tal que (0 ≤ i, j, k < (|s| − 1)) y (i + 2 = j + 1 = k) y
(s[i] = s[j] = s[k])) }
}'''

def iguales_consecutivos(lista: list[int]) -> bool:
    for indice in range(len(lista) - 2):
        if lista[indice] == lista[indice + 1] == lista[indice + 2]:
            return True
    return False
        
print(iguales_consecutivos([1,2,3,3,4]))
print(iguales_consecutivos([1,1,1,2,4,5]))
print(iguales_consecutivos([1,2,4,5]))
print(iguales_consecutivos([0,1,2,3,4,5,6,7,8,9,9,9]))
