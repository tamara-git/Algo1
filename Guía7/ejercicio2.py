# Ejercicio 2
'''1. problema CerosEnPosicionesPares (inout s:seq⟨Z⟩) {
requiere: { T rue }
modifica: { s }
asegura: { (|s| = |s@pre|) y (para todo i entero, con 0 <= i < |s|, si i es impar entonces s[i] = s@pre[i] y, si i
es par, entonces s[i] = 0) }
}'''

def cerosEnPosicionesPares(secuencia:list[int]) -> None:
    for i in range (len(secuencia)):
        if i % 2 == 0:
            secuencia[i] = 0

mi_lista : list[int] = [1,2,3,4,79]
cerosEnPosicionesPares(mi_lista)
print(mi_lista)

'''2. problema CerosEnPosicionesPares2 (in s:seq⟨Z⟩) : seq⟨Z⟩ {
requiere: { T rue }
asegura: { (|s| = |res|) y (para todo i entero, con 0 <= i < |res|, si i es impar entonces res[i] = s[i] y, si i es
par, entonces res[i] = 0) }
}'''

def cerosEnPosicionesPares2(lista: list[int]) -> list[int]:
    lista_copia: list[int] = lista.copy()
    for i in range (len(lista_copia)):
        if i % 2 == 0:
            lista_copia[i] = 0
    return lista_copia

print(cerosEnPosicionesPares2([5,6,4,7,3,6]))

'''3. Dada una cadena de caracteres devuelva una cadena igual a la anterior, pero sin las vocales. No se agregan espacios,
sino que borra la vocal y concatena a continuaci´on.
problema sin vocales (in s:seq⟨Char⟩) : seq⟨Char⟩ {
requiere: { T rue }
asegura: { res es la subsecuencia de s que se obtiene al quitarle las vocales a s }
}
Nota: Una subsecuencia de una cadena es una nueva secuencia que se crea eliminando algunos elementos de la cadena
original, conservando el orden de los elementos restantes.
'''

def sin_vocales(cadena:str) -> str:
    cadena_nueva: str = ""
    for i in range(len(cadena)):
        if cadena[i] not in "aeiou" and cadena[i] not in "AEIOU":
            cadena_nueva += cadena[i]
        else:
            cadena_nueva += ""
    return cadena_nueva

print(sin_vocales("Tamara Diana Argañaraz"))

'''4. problema reemplaza vocales (in s:seq⟨Char⟩) : seq⟨Char⟩ {
requiere: { T rue }
asegura: { |res| = |s| }
asegura: { Para todo i ∈ Z, si 0 ≤ i < |res| → (pertenece(<'a','e','i','o','u'>, s[i]) ∧ res[i] = ‘ ’) ∨
(¬ pertenece(<'a','e','i','o','u'>, s[i]) ∧ res[i] = s[i])) }
}
'''

def reemplaza_vocales(cadena:str) -> str:
    cadena_nueva: str = ""
    for i in range(len(cadena)):
        if cadena[i] not in "aeiou" and cadena[i] not in "AEIOU":
            cadena_nueva += cadena[i]
        else:
            cadena_nueva += " "
    return cadena_nueva

print(reemplaza_vocales("tamara Diana"))

'''5. problema da vuelta str (in s:seq⟨Char⟩) : seq⟨Char⟩ {
requiere: { T rue }
asegura: { |res| = |s| }
asegura: { Para todo i ∈ Z si 0 ≤ i < |res| → res[i] = s[|s| - i - 1] }
}
'''

def da_vuelta_str(cadena:str) -> str:
    cadena_nueva: str = "" 
    for i in range(len(cadena)-1,-1,-1):
        cadena_nueva += cadena[i]
    return cadena_nueva

print(da_vuelta_str("tamara"))

'''6. problema eliminar repetidos (in s:seq⟨Char⟩) : seq⟨Char⟩ {
requiere: { T rue }
asegura: { (|res| ≤ |s|) ∧ (para todo i ∈ Z si 0 ≤ i < |s| → pertenece(s[i], res)) ∧ (para todo i, j ∈ Z si
(0 ≤ i, j < |res| ∧ i ̸= j) → res[i] ̸= res[j]) }
}'''


def eliminar_repetidos(cadena:str) -> str:
    sin_repetidos: str = ""
    for i in range(len(cadena)):
        if cadena[i] != sin_repetidos:
            sin_repetidos += cadena[i]
        else:
            sin_repetidos += ""
    return sin_repetidos


print(eliminar_repetidos("tamara"))

'''Ejercicio 3. Implementar una funci´on para conocer el estado de aprobaci´on de una materia a partir de las notas obtenidas
por un/a alumno/a cumpliendo con la siguiente especificaci´on:
problema resultadoMateria (in notas: seq⟨Z⟩) : Z {
requiere: { |notas| > 0 }
requiere: { Para todo i ∈ Z si 0 ≤ i < |notas| → 0 ≤ notas[i] ≤ 10) }
asegura: { res = 1 ↔ todos los elementos de notas son mayores o iguales a 4 y el promedio es mayor o igual a 7 }
asegura: { res = 2 ↔ todos los elementos de notas son mayores o iguales a 4 y el promedio est´a entre 4 (inclusive) y 7 }
asegura: { res = 3 ↔ alguno de los elementos de notas es menor a 4 o el promedio es menor a 4 }
}'''

def promedio(notas:list[int]) -> int:
    suma_notas: int = 0
    total: int = 0
    promedio: int = 0
    for i in range(len(notas)):
        suma_notas += notas[i]
        total += 1
    promedio = suma_notas/total
    return promedio 
    
print(promedio([1,2,3,4]))

    
def resultadoMateria(notas: list[int]) -> int:
    res: int = 0
    for i in range(len(notas)):
        if notas[i] >= 4 and promedio(notas) >= 7:
            res = 1 
        if notas[i] >= 4 and 4 <= promedio(notas) < 7:
            res = 2
        else:
            res = 3
    return res

print(resultadoMateria([10,7,4,6,4]))

'''Ejercicio 4. Dada una lista de tuplas, que representa un historial de movimientos en una cuenta bancaria, devolver el saldo
actual. Asumir que el saldo inicial es 0. Las tuplas tienen una letra que nos indica el tipo de movimiento “I” para ingreso
de dinero y “R” para retiro de dinero, y adem´as el monto de cada operaci´on. Por ejemplo, si la lista de tuplas es [("I",
2000), ("R", 20),("R", 1000),("I", 300)] entonces el saldo actual es 1280.
problema saldoActual (in movimientos: seq⟨Char × Z⟩) : Z {
requiere: { Para todo i ∈ Z si 0 ≤ i < |movimientos| → movimientos[i]0 ∈ {“I”,“R”} y movimientos[i]1 > 0 }
asegura: { res =
Pingresos
i movimientos[i]1 −
Pretiros
i movimientos[i]1 }
}'''

def saldoActual(movimientos:list[tuple[str,int]]) -> int:
    saldo_actual: int = 0
    for i in range(len(movimientos)):
        if movimientos[i][0] == "I":
            saldo_actual += movimientos[i][1]
        else:
            saldo_actual -= movimientos[i][1]
    return saldo_actual

print(saldoActual([("I",
2000), ("R", 20),("R", 1000),("I", 300)]))
