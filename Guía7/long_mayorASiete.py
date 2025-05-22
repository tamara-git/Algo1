'''Dada una lista de palabras (seq⟨seq⟨Char⟩⟩), devolver verdadero si alguna palabra tiene longitud mayor a 7. Ejemplo:
[“termo”, “gato”, “tener”, “jirafas”], devuelve falso.
problema long mayorASiete (in s:seq⟨seq⟨Char⟩⟩) : Bool {
requiere: { T rue }
asegura: { (res = true) ↔ (existe i ∈ Z tal que (0 ≤ i < (|s| − 1)) y (|s[i]| > 7) }
}
'''

def long_mayorASiete(lista: list[str]) -> bool:
    for indice in range (len(lista)):
        if len(lista[indice]) >= 7:
            return False
    else:
        return True
print(long_mayorASiete(["termo","gato","tener","caca"]))
print(long_mayorASiete(["termo","gato","tener","jirafas"]))