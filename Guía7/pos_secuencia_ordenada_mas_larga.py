'''Recorrer una seq⟨Z⟩ y devolver la posición donde inicia la secuencia de números ordenada más larga. Si hay dos
subsecuencias de igual longitud devolver la posición donde empieza la primera. La secuencia de entrada es no vac´ıa.
problema pos secuencia ordenada mas larga (in s:seq⟨Z⟩) : Z {
requiere: { |s| > 0 }
asegura: { (res = i) ↔ (existe i, j ∈ Z tal que (0 ≤ i, j < (|s| − 1)) y i ≤ j y (para todo k tal que i ≤ k < j →
s[k] ≤ s[k + 1]) y j-i+1 es máximo e i es el mínimo valor que lo cumple) }
}
'''

def pos_secuencia_mas_larga(lista: list[int]) -> int:
    secuencia_ordenada: list[int] = []
    contador: int = 0
    for indice in range(len(lista)):
        if lista[indice] < lista[indice + 1]:
            secuencia_ordenada += lista[indice] + lista[indice + 1]

    for indice in range(len(lista)):
        


        