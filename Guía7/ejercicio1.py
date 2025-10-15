'''1. problema pertenece (in s:seq⟨Z⟩, in e: Z) : Bool {
requiere: { T rue }
asegura: { (res = true) ↔(existe un i ∈ Z tal que 0 ≤ i < |s| ∧ s[i] = e) }
}
Implementar al menos de 3 formas distintas este problema.
'''

def pertenece(s: list[int], e: int) -> bool:
    res = False
    for elem in s:
        if elem == e:
            res = True
    return res

print(pertenece([1,2,3,4], 1))

def pertenece_2 (secuencia: list[int], elemento: int) -> bool:
    res: bool = False
    for i in range(0,len(secuencia)-1):
        if elemento == secuencia[i]:
            res = True
    return res 

        
print(pertenece_2([1,2,3,4], 5))

def pertenece_3 (secuencia: list[int], elemento: int) -> bool:
    i: int = 0
    res: bool = False
    while i <= (len(secuencia)-1) and res == False:
        if elemento != secuencia[i]:
            res = False
            i += 1
        else: 
            res = True
    return res 
        
print(pertenece_3([1,2,3,4], 6))

'''2.problema divide a todos (in s:seq⟨Z⟩, in e: Z) : Bool {
requiere: { e ̸= 0 }
asegura: { (res = true) ↔ (para todo i ∈ Z si 0 ≤ i < |s| → s[i] mod e = 0) }
}'''

def divide_a_todos (secuencia:list[int], numero: int) -> bool:
    res = True
    for elemento in secuencia:
        if elemento % numero != 0:
            res = False 
    return res


print(divide_a_todos([20,4,40,8,1], 2))

'''3. problema suma total (in s:seq⟨Z⟩) : Z {
requiere: { T rue }
asegura: { res es la suma de todos los elementos de s }
}
Nota: no utilizar la funci´on sum() nativa'''

def suma_total (secuencia: list[int]) -> int:
    res: int = 0
    for i in range(0,len(secuencia)):
        res += secuencia[i]
    return res

print(suma_total([1,7]))

'''4. problema maximo (in s:seq⟨Z⟩) : Z {
requiere: { |s| > 0 }
asegura: { res = al mayor de todos los n´umeros que aparece en s }
}
Nota: no utilizar la funci´on max() nativa.'''

def maximo (secuencia: list[int]) -> int:
    maximo: int = secuencia[0]
    for i in range (1,len(secuencia)):
        if maximo < secuencia [i]:
            maximo = secuencia[i]
    return maximo

print(maximo([9000000,4,7900,50000]))

'''5. problema minimo (in s:seq⟨Z⟩) : Z {
requiere: { |s| > 0 }
asegura: { res = al menor de todos los n´umeros que aparece en s }
}
Nota: no utilizar la funci´on min() nativa.'''

def minimo (secuencia: list[int]) -> int:
    minimo: int = secuencia[0]
    for i in range (1,len(secuencia)):
        if minimo > secuencia [i]:
            minimo = secuencia[i]
    return minimo

print(minimo([9000000,4,7900,50000]))

'''6. problema ordenados (in s:seq⟨Z⟩) : Bool {
requiere: { T rue }
asegura: { res = true ↔(para todo i ∈ Z si 0 ≤ i < (|s| − 1) → s[i] < s[i + 1] }
}'''

def ordenados(secuencia: list[int]) -> bool:
    menor: int = secuencia[0]
    res: bool = False 
    for i in range (1,len(secuencia)):
        if menor < secuencia[i]:
            res = True
            menor = secuencia[i]
        else: 
            res = False 
    return res 

print(ordenados([3,7,8,9]))

'''7. problema pos maximo (in s:seq⟨Z⟩) : Z {
requiere: { T rue }
asegura: { (Si |s| = 0, entonces res = −1; si no, res = al ´ındice de la posici´on donde aparece el mayor elemento
de s (si hay varios es la primera aparici´on) }
}'''

def pos_maximo(secuencia:list[int]) -> int:
    res: int = 0
    maximo: int = secuencia[0]
    if len(secuencia) == 0:
        res = -1
    else:
        for i in range(1,len(secuencia)):
            if maximo < secuencia [i]:
                maximo = secuencia[i]
                res = i
            else:
                res = res
        return res 

print(pos_maximo([1,4000000,200,4,6000,10])) 

'''8. problema pos minimo (in s:seq⟨Z⟩) : Z {
requiere: { T rue }
asegura: { (Si |s| = 0, entonces res = −1; si no, res = al ´ındice de la posici´on donde aparece el menor elemento
de s (si hay varios es la ´ultima aparici´on) }
}'''

def pos_minimo(secuencia:list[int]) -> int:
    res: int = 0
    minimo: int = secuencia[0]
    if len(secuencia) == 0:
        res = -1
    else:
        for i in range (1,len(secuencia)):
            if minimo > secuencia[i]:
                res = i
            else:
                res = res
        return res

print(pos_minimo([-1,400000000,200,4,-60,-1000])) 


'''9. Dada una lista de palabras (seq⟨seq⟨Char⟩⟩), devolver verdadero si alguna palabra tiene longitud mayor a 7. Ejemplo:
[“termo”, “gato”, “tener”, “jirafas”], devuelve falso.
problema long mayorASiete (in s:seq⟨seq⟨Char⟩⟩) : Bool {
requiere: { True }
asegura: { (res = true) ↔ (existe i ∈ Z tal que (0 ≤ i < (|s| − 1)) y (|s[i]| > 7) }
}'''

def long_mayorASiete(lista_de_palabras: list[str]) -> bool:
    res: bool = False 
    for i in range(len(lista_de_palabras)):
        if len(lista_de_palabras[i]) <= 7:
            res = False 
        else:
            res = True 
    return res

print(long_mayorASiete(["hola","como","estas","farmacias"]))

'''10.Dado un texto en formato string, devolver verdadero si es pal´ındromo (se lee igual en ambos sentidos), falso en caso
contrario. Las cadenas de texto vac´ıas o con 1 s´olo elemento son pal´ındromo.
problema es palindroma (in s:seq⟨Char⟩) : Bool {
requiere: { T rue }
asegura: { (res = true) ↔ (s es igual a su reverso) }
}'''

def palabra_inversa(palabra:str) -> str:
    palabra_inversa: str = ""
    for i in range(len(palabra)-1,-1,-1):
        palabra_inversa += palabra[i]
    return palabra_inversa

print(palabra_inversa("aca"))

def es_palindroma(palabra: str) -> bool:
    return palabra == palabra_inversa(palabra)
 

print(es_palindroma("aca"))

'''11. Recorrer una seq⟨Z⟩ y devolver verdadero si hay 3 n´umeros iguales consecutivos, en cualquier posici´on y False en caso
contrario.
problema iguales consecutivos (in s:seq⟨Z⟩) : Bool {
requiere: { T rue }
asegura: { (res = true) ↔ (existe i, j, k ∈ Z tal que (0 ≤ i, j, k < (|s| − 1)) y (i + 2 = j + 1 = k) y
(s[i] = s[j] = s[k])) }
}'''

def iguales_consecutivos(secuencia:list[int]) -> bool:
    res: bool = False
    for i in range(len(secuencia)-2):
        if secuencia[i] == secuencia[i+1] == secuencia[i+2]:
            res = True 
    return res

print(iguales_consecutivos([0,1,1,2,4,4,5]))


'''12. Recorrer una palabra en formato string y devolver True si ´esta tiene al menos 3 vocales distintas y False en caso
contrario.
problema vocales distintas (in s:seq⟨Char⟩) : Bool {
requiere: { True }
asegura: { (res = true) ↔ (existe i, j, k ∈ Z tal que (0 ≤ i, j, k < (|s| − 1)) y (s[i]̸ = s[j]̸ = s[k]) y
(s[i], s[j], s[k] ∈ {‘a‘, ‘e‘, ‘i‘, ‘o‘, ‘u‘})) }
}'''

def vocales_minusculas(letra:str) -> str:
    vocal: str = ''
    if letra =='a' or letra == 'A':
        vocal = 'a'
    if letra =='e' or letra == 'E':
        vocal = 'e'
    if letra =='i' or letra == 'I':
        vocal = 'i'
    if letra =='o' or letra == 'O':
        vocal = 'o'
    if letra =='u' or letra == 'U':
        vocal ='u'
    if (letra not in "aeiou") and (letra not in "AEIOU"):
        vocal = ''
    return vocal

print(vocales_minusculas('E'))

def sin_consonantes(palabra:str) -> str:
    palabra_sin_consonantes: str = ''
    for i in range (len(palabra)):
        palabra_sin_consonantes += vocales_minusculas(palabra[i])
    return palabra_sin_consonantes

print(sin_consonantes("tAmarA"))

def vocales_distintas(palabra:str) -> bool:
    vocales_dif: int = 0
    primer_vocal: str = sin_consonantes(palabra)[0]
    res: bool = False
    for i in range(1,len(sin_consonantes(palabra))):
        if primer_vocal != sin_consonantes(palabra)[i]:
            vocales_dif += 2
        else:
            primer_vocal = sin_consonantes(palabra)[i]
    if vocales_dif >= 3:
        res = True 
    else:
        res = False
    return res
        
print(vocales_distintas("mateo"))

'''13. Recorrer una seq⟨Z⟩ y devolver la posici´on donde inicia la secuencia de n´umeros ordenada m´as larga. Si hay dos
subsecuencias de igual longitud devolver la posici´on donde empieza la primera. La secuencia de entrada es no vac´ıa.
problema pos secuencia ordenada mas larga (in s:seq⟨Z⟩) : Z {
requiere: { |s| > 0 }
asegura: { (res = i) ↔ (existe i, j ∈ Z tal que (0 ≤ i, j < (|s| − 1)) y i ≤ j y (para todo k tal que i ≤ k < j →
s[k] ≤ s[k + 1]) y j-i+1 es m´aximo e i es el m´ınimo valor que lo cumple) }
}'''

def pos_secuencia_ordenada_mas_larga_aux(secuencia:list[int]) -> int:
    indice: int = 0
    indice_max: int = 0
    cant_elementos: int = 1
    max_cant: int = 0
    for i in range(len(secuencia)-1):
        if secuencia[i] <= secuencia[i+1]:
            cant_elementos += 1
        else:
            if cant_elementos > max_cant:
                max_cant = cant_elementos
                indice_max = indice
                indice = i+1
            cant_elementos = 1
    if cant_elementos > max_cant:
        indice_max = indice
    return indice_max
        

        
print(pos_secuencia_ordenada_mas_larga_aux([1,2,3,5,6,7,1,2,3,4,5,6,1,2]))

'''14. Cantidad de d´ıgitos impares.
problema cantidad digitos impares (in s:seq⟨Z⟩) : Z {
requiere: { Todos los elementos de n´umeros son mayores o iguales a 0 }
asegura: { res es la cantidad total de d´ıgitos impares que aparecen en cada uno de los elementos de n´umeros }
}
Por ejemplo, si la lista de n´umeros es [57, 2383, 812, 246], entonces el resultado esperado ser´ıa 5 (los d´ıgitos impares
son 5, 7, 3, 3 y 1)'''

def contar_digitos_impares(numero: int) -> int:
    contador: int = 0
    for i in range(len(str(numero))):
        if int(str(numero)[i]) % 2 != 0:
            contador += 1
    return contador 


def cantidad_digitos_impares(secuencia:list[int]) -> int:
    contador: int = 0
    for i in range(len(secuencia)):
        contador += contar_digitos_impares(secuencia[i])
    return contador

print(cantidad_digitos_impares([57, 2383, 812, 246]))