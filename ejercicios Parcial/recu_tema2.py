#Ejercicio 1
def gestion_de_ventas(ventas_empleado_producto: list[tuple[str,str,int]]) -> dict[str,tuple[str,int]]:
    res: dict[str,tuple[str,int]] = {}
    for i in range(len(ventas_empleado_producto)):
        empleado: str =  ventas_empleado_producto[i][0]
        producto: str = ventas_empleado_producto[i][1]
        cantidad_ventas: int = ventas_empleado_producto[i][2]
        if producto not in res.values():
            res[empleado] = (producto, cantidad_ventas)
    return res

#Ejercicio 2
def digitos_impares(numero: int) -> int:
    cantidad: int = 0
    num_str: str = str(numero)
    for indice in range(len(num_str)):
        if int(num_str[indice]) % 2 != 0:
            cantidad += 1
    return cantidad

def cantidad_digitos_impares(numeros: list[int]) -> int:
    cantidad: int = 0
    for indice in range(len(numeros)):
        numero: int = numeros[indice]
        cantidad += digitos_impares(numero)
    return cantidad

print(cantidad_digitos_impares([57,2383,812,246]))

#Ejercicio 3
from queue import Queue as Cola
def reordenar_cola_primero_numerosas(carpetas: Cola[tuple[str,int]], umbral:int) -> Cola[tuple[str,int]]:
    cola_aux: Cola[tuple[str,int]] = Cola()
    colaConMayores: Cola[tuple[str,int]] = Cola()
    colaConMenores: Cola[tuple[str,int]] = Cola()
    res: Cola[tuple[str,int]] = Cola()

    while not carpetas.empty():
        tupla: tuple[str,int] = carpetas.get()
        cola_aux.put(tupla)
        num_paginas: int = tupla[1]
        if num_paginas > umbral:
            colaConMayores.put(tupla)
        else:
            colaConMenores.put(tupla)

    while not colaConMayores.empty():
        tupla: tuple[str,int] = colaConMayores.get()
        res.put(tupla)
    
    while not colaConMenores.empty():
        tupla: tuple[str,int] = colaConMenores.get()
        res.put(tupla)
    
    while not cola_aux.empty():
        tupla: tuple[str,int] = cola_aux.get()
        carpetas.put(tupla)
    return res

#Ejercicio 4
def maximo(lista: list[int]) -> int:
    maximo: int = lista[0]
    for i in range(len(lista)):
        elemento: int = lista[i]
        if elemento > maximo:
            maximo = elemento
    return maximo


def columna(m: list[list[int]], columna: int) -> list[int]:
    col: list[int] = []
    for i in range(len(m)):
        col.append(m[i][columna])
    return col

def matriz_cuasi_decreciente(matriz: list[list[int]]) -> bool:
    maximo: int = columna(matriz,0)
    res: bool = True
    for indice in range(len(matriz[0])):
        if columna(matriz, indice) > maximo:
            res = False
    return res 
    


