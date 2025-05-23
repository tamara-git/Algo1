'''Cantidad de dígitos impares.
problema cantidad digitos impares (in s:seq⟨Z⟩) : Z {
requiere: { Todos los elementos de números son mayores o iguales a 0 }
asegura: { res es la cantidad total de dígitos impares que aparecen en cada uno de los elementos de números }
}
Por ejemplo, si la lista de números es [57, 2383, 812, 246], entonces el resultado esperado sería 5 (los dígitos impares
son 5, 7, 3, 3 y 1).
'''
def numero_a_listaDigitos(numero:int) -> list[int]:
    acumulador: list = []
    lista_str_digitos_numero = list(str(numero))
    for indice in range (len(lista_str_digitos_numero)):
        lista_str_digitos_numero[indice] = int(lista_str_digitos_numero[indice])
        acumulador = acumulador + [lista_str_digitos_numero[indice]]
    return acumulador

print(numero_a_listaDigitos(57))

# Ahora tengo que pasar una lista de números a una que tenga los digitos de cada número.
def lista_numeros_a_listaDigitos(lista:list[int]) -> list[int]:
    acumulador : list = []
    for elemento in lista:
        acumulador = acumulador + numero_a_listaDigitos(elemento) 
    return acumulador

print(lista_numeros_a_listaDigitos([57,15]))

def cantidad_digitos_impares(lista:list[int]) -> int:
    cantidad_digitos_impares : int = 0
    lista: list = lista_numeros_a_listaDigitos(lista)
    for elemento in lista:
        if elemento % 2 == 1:
            cantidad_digitos_impares += 1
    return cantidad_digitos_impares

print(cantidad_digitos_impares([66, 2486, 822, 241]))