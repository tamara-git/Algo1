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
    