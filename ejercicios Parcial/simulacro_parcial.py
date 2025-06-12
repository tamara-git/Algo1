'''problema maximas_cantidades_consecutivos (in v: seq⟨Z⟩) :
Diccionario⟨Z,Z⟩ {
requiere: { True }
asegura: { Las claves de res son exactamente los números que
aparecen al menos una vez en v }
asegura: { Para cada clave k de res, su valor es igual a la
máxima cantidad de apariciones consecutivas de k en v, donde
dicha cantidad de apariciones es mayor o igual 1. }
}
'''

def maximas_cantidades_consecutivos(v: list[int]) -> dict[int,int]:
    dict[int,int] = {}


# me armo una función que cuente la cantidad de apariciones del numero en v
def cantidad_de_apariciones_consecutivos(v: list[int], numero: int) -> int:
    cantidad_apariciones: int = 0

    for indice in range(len(v)-1):
        if numero == v[indice]:
            if numero == v[indice + 1] :
                cantidad_apariciones += 2
            else:
                cantidad_apariciones += 1

    return cantidad_apariciones

print(cantidad_de_apariciones_consecutivos([4,4,4,8,1,1,1], 1))

'''problema maxima_cantidad_primos(in A: seq⟨seq⟨Z⟩⟩) : Z {
requiere: { Todas las filas de A tienen la misma longitud }
asegura: { Existe alguna columna c en A para la cual res de sus
elementos son números primos }
asegura: { Todas las columnas de A tienen a lo sumo res
elementos que son números primos }
}
'''
# si tiene más de 4 divisores, no es primo
def es_primo(numero:int) -> bool:
    numero_divisor: int = 1
    divisores: int = 0
    while divisores < 4:
        if numero % numero_divisor == 0:
            numero_divisor += 1
            divisores += 2

    if divisores != 4:
        return False
    return True


def maximo_elemento(lista: list[int]) -> int:
    maximo: int = lista[0]

    for indice in range(len(lista)-1):
        if lista[indice] < lista[indice + 1]:
            maximo = lista[indice + 1]

    return maximo


def maxima_cantidad_primos(A: list[list[int]]) -> int:
    lista_cantidad_primos: list[int] = []

    filas: int = len(A)
    columnas: int = len(A[0])

    for columna in range(columnas):
        cantidad_primos: int = 0
        for fila in range(filas):
            if es_primo(A[fila][columna]) == True:
                cantidad_primos += 1
            lista_cantidad_primos.append(cantidad_primos)

    return maximo_elemento(lista_cantidad_primos)

print(maxima_cantidad_primos([[1,11,5],[0,2,10],[2,7,9]]))