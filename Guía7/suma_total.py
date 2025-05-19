'''problema suma total (in s:seq⟨Z⟩) : Z {
requiere: { True }
asegura: { res es la suma de todos los elementos de s }
}'''
def suma_total(s:list[int]) -> int:
    suma : int = 0 
    for elem in s:
        suma = suma + elem

def suma_total_2 (lista:list[int]) -> int:
    suma : int = 0
    for indice in range (len[lista]):
        suma = suma + lista[indice]
