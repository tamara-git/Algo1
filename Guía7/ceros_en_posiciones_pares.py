'''problema CerosEnPosicionesPares (inout s:seq⟨Z⟩) {
requiere: { True }
modifica: { s }
asegura: { (|s| = |s@pre|) y (para todo i entero, con 0 <= i < |s|, si i es impar entonces s[i] = s@pre[i] y, si i
es par, entonces s[i] = 0) }
}'''

def CerosEnPosicionesPares(lista:list[int]) -> None:
    for indice in range(len(lista)):
        if indice % 2 == 0:
            lista[indice] = 0
