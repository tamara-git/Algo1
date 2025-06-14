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
def cantidad_apariciones(lista:list[int], numero: int) -> int:
    aparicion: int = 0
    for indice in range(len(lista)-1):
        if numero == lista[indice]:
            aparicion += 1

    return aparicion

def cantidad_de_apariciones_consecutivos(v: list[int], numero: int) -> int:
    apariciones_consecutivas: int = 0
    for indice in range(len(v)-2):
        if numero == v[indice] and numero == v[indice + 1]:
            apariciones_consecutivas += 2 
        elif numero == v[indice] and numero != v[indice + 1]:
            apariciones_consecutivas += 1
        else:
            apariciones_consecutivas += 0
        
    return apariciones_consecutivas

#print(cantidad_de_apariciones_consecutivos([4,4,4,8,1,1,1], 4))

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

    if numero < 0:
        numero = -numero

    numero_divisor: int = 0
    divisores: int = 0
    while numero_divisor <= numero:
        if numero == 0:
            break
        numero_divisor += 1
        if numero % numero_divisor == 0:
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

'''problema resolver_cuenta(in s: string): R {
requiere: { Cada caracter de s es '+', '-', '.' (separador decimal)
o es un dígito }
requiere: { No hay dos operadores consecutivos en s (los
operadores son '+' y '-') }
requiere: { El último caracter de s es un dígito }
requiere: { El primer caracter de s es un dígito o un operador }
requiere: { En las posiciones adyacentes a cada aparición de '.'
en s, hay un dígito }
requiere: { Entre un operador y el operador inmediato
siguiente hay a lo sumo un separador decimal }
requiere: { Antes del primer operador hay a lo sumo un
separador decimal }
requiere: { Después del último operador hay a lo sumo un
separador decimal }
asegura: { res es igual al resultado de la operación aritmética
representada por s }
}
Hint: las funciones int o float permiten convertir strings en
números enteros o flotantes respectivamente.
Ejemplo: Para el input "+10" se debe devolver 10.'''


def resolver_cuenta(s:str) -> float:
    nueva_cadena: str = ""
    sumar_o_restar: float = 0.0
    n: int = 0

    for indice in range(len(s)):
        if s[0] not in ['+','-']:
            for indice in range(3):
                nueva_cadena += s[indice]
            sumar_o_restar += float(nueva_cadena)
            nueva_cadena = ""
            for indice in range(n+3, n+7):
                nueva_cadena += s[indice]
            sumar_o_restar += float(nueva_cadena)
            nueva_cadena = ""
            if (n + 7) < len(s):
                n += 4
            else: 
                break
        else:
            for indice in range(n, n+4):
                nueva_cadena += s[indice]
            sumar_o_restar += float(nueva_cadena)
            nueva_cadena = ""
            if (n + 4) < len(s):
                n += 4
            else: 
                break
    return sumar_o_restar 

        

print(resolver_cuenta("5.0 - 4.0"))