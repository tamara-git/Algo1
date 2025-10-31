# 1) Códigos filtrados [2 puntos]
# El hijo del dueño de la veterinaria, cuya actividad principal es ver tik toks, cree que los productos 
# cuyos código de barras terminimoan en números primos son especialmente auspiciosos y deben ser destacados
# en la tienda. Luego de convencer a su padre de esta idea, solicita una función en python que facilite
# esta gestión.
# Se pide implementar una función que, dada una secuencia de enteros, cada uno representando un código 
# de barras de un producto, cree y devuelva una nueva lista que contenga únicamente aquellos números de 
# la lista original cuyos últimos tres dígitos formen un número primo (por ejemplo, 101, 002 y 011).

# Nota: un número primo es aquel que solo es divisible por si mismo y por 1. Algunos ejemplos de hasta 
# tres dígitos son 2, 3, 4, 101, 103, 107, etc.

# problema filtrar_codigos_primos(in codigos_barra: seq<Z>) : seq<Z> {
# requiere: {Todos los enteros de codigos_barra tienen, por lo menos, 3 dígitos}
# requiere: {No hay elementos repetidos en codigos_barra}
# asegura: {los últimos 3 dígitos de cada uno de los elementos de res forman un número primo}
# asegura: {Todos los elementos de codigos_barra cuyos últimos 3 dígitos forman un número primo 
# están en res}
# asegura: {Todos los elementos de res están en codigos_barra}
# }


def es_primo(numero:int) -> bool:
    divisores: int = 0
    res: bool = True
 
    for divisor in range(1,numero+1):
        if numero % divisor == 0:
            divisores += 1
    if divisores > 2:
        res = False 

    return res

def ult_3_digitos(numero:int) -> int:
    numero_str: str = str(numero)
    res: str = ""
    if len(numero_str) < 3:
        res = str(numero)
    else:
        for i in range(len(numero_str)-3,len(numero_str)):
            res += numero_str[i]
    return int(res)

print(ult_3_digitos(101))




def filtrar_codigos_primos(codigos_barra: list[int]) -> list[int]:
    res: list[int] = []
    for i in range(len(codigos_barra)):
        numero: int = codigos_barra[i]
        if es_primo(ult_3_digitos(numero)):
            res.append(ult_3_digitos(numero))
    return res

print(filtrar_codigos_primos([12,15,11,900,101,7,17,103,107]))
