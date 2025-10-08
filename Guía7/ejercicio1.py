'''1. problema pertenece (in s:seq⟨Z⟩, in e: Z) : Bool {
requiere: { T rue }
asegura: { (res = true) ↔(existe un i ∈ Z tal que 0 ≤ i < |s| ∧ s[i] = e) }
}
Implementar al menos de 3 formas distintas este problema.
'''

def pertenece (secuencia: list[int], elemento: int) -> bool:
    res: bool = True
    for elem in secuencia:
        if elem == elemento or elemento == (len(secuencia)-1):
            res = True
        else:
            res = False
    return res

print(pertenece([1,2,3,4], 5))

def pertenece_2 (secuencia: list[int], elemento: int) -> bool:
    res: bool = True
    for i in range(0,len(secuencia)-1):
        if elemento == secuencia[(len(secuencia)-1)] or elemento == secuencia[i]:
            res = True
        else:
            res = False 
    return res 

        
print(pertenece_2([1,2,3,4], 5))

def pertenece_3 (secuencia: list[int], elemento: int) -> bool:
    i: int = 0
    res: bool = True
    while i <= (len(secuencia)-1): 
