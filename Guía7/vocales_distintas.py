'''Recorrer una palabra en formato string y devolver True si esta tiene al menos 3 vocales distintas y
 False en caso contrario.
problema vocales distintas (in s:seq⟨Char⟩) : Bool {
requiere: { True }
asegura: { (res = true) ↔ (existe i, j, k ∈ Z tal que (0 ≤ i, j, k < (|s| − 1)) y (s[i] ̸= s[j] ̸= s[k]) y
(s[i], s[j], s[k] ∈ {‘a‘, ‘e‘, ‘i‘, ‘o‘, ‘u‘})) }
}
'''
vocales = ['a','e','i','o','u']
def vocales_en_palabra(lista:list[str]) -> list[str]:
    vocales_en_palabra : list = []
    for indice in range(len(lista)):
        if lista[indice] in vocales:
            vocales_en_palabra = vocales_en_palabra + [lista[indice]]
    return vocales_en_palabra

print(vocales_en_palabra(['h','o','l','a','u']))

def sinRepeticion(lista: list[str]) -> bool:
    lista: list = vocales_en_palabra(lista)
    vocales_diferentes = 0
    if len((lista)) < 3:
        return False
    else:
        for indice in range(len(lista)-1): 
            for indice2 in range(indice + 1,len(lista)):
                if not(lista[indice] == lista [indice2]):
                    vocales_diferentes += 1
    if vocales_diferentes >= 3:
        return True
    else:
        return False

print(sinRepeticion(['h','l','a','a','o']))








    







                        
'''   def vocales_distintas(lista:list[str]) -> bool:
    for indice in range(len(vocales_en_palabra(lista))):
        if iguales_consecutivos(vocales_en_palabra(lista)) == True:
            return False
    else: 
        return True
print(vocales_distintas(['t','a','m','a','r','a']))
print(vocales_distintas(['t','a','m','i']))
print(vocales_distintas(['t','a','m','a','t','u']))'''