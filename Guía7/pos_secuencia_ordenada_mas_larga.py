'''
Recorrer una seq⟨Z⟩ y devolver la posición donde inicia la secuencia de números ordenada más larga. Si hay dos
subsecuencias de igual longitud devolver la posición donde empieza la primera. La secuencia de entrada es no vac´ıa.
problema pos secuencia ordenada mas larga (in s:seq⟨Z⟩) : Z {
requiere: { |s| > 0 }
asegura: { (res = i) ↔ (existe i, j ∈ Z tal que (0 ≤ i, j < (|s| − 1)) y i ≤ j y (para todo k tal que i ≤ k < j →
s[k] ≤ s[k + 1]) y j-i+1 es máximo e i es el mínimo valor que lo cumple) }
}
'''

def pos_secuencia_mas_larga(lista: list[int]) -> int:
    contador_mayor: int = 0   
    contador: int = 1 
    guarda_primer_indice: list[int] = []
    for indice in range(len(lista)-1):
        if lista[indice] < lista[indice + 1]:
            guarda_primer_indice.append(indice)
            contador += 1
            if contador != 2:
                guarda_primer_indice.pop()
        else: 
              if contador_mayor < contador:
                contador_mayor = contador
                contador = 1
    
    return guarda_primer_indice.pop()

        
print(pos_secuencia_mas_larga([0,1,2,3,5,1,2,3,4,5,6,0,1,2,4,5,6,7,8,9]))
        