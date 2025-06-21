'''Sala de Escape - Promedio de salidas
Un grupo de amigos apasionados por las salas de escape, llevan un registro meticuloso de todas las salas de escape que hay en Capital.
 Este registro indica si han visitado una sala y si pudieron o no salir de ella. 
 Un 0 significa que no fueron, un 61 que no lograron salir a tiempo,
y un n´umero entre 1 y 60 representa los minutos que les tom´o escapar exitosamente. Con estos datos, pueden comparar sus
logros y desafíos en cada nueva aventura que emprenden juntos.
Dado un diccionario donde la clave es el nombre de cada amigo y el valor es una lista de los tiempos (en minutos) registrados
para cada sala de escape en Capital, escribir una funci´on en Python que devuelva un diccionario. En este nuevo diccionario,
las claves deben ser los nombres de los amigos y los valores deben ser tuplas que indiquen la cantidad de salas de las que cada
persona logr´o salir y el promedio de los tiempos de salida (solo considerando las salas de las que lograron salir).
problema promedio de salidas (in registro: dict<str, seq⟨Z⟩>) : dict<str, <Z×R>> {
requiere: {registro tiene por lo menos un integrante.}
requiere: {Todos los integrantes de registro tiene por lo menos un tiempo.}
requiere: {Todos los valores de registro tiene la misma longitud.}
requiere: {Todos los tiempos de los valores de registro est´an entre 0 y 61 inclusive.}
asegura: {res tiene las mismas claves que registro.}
asegura: {El primer elemento de la tupla de res para un integrante, es la cantidad de salas con tiempo mayor estricto a
0 y menor estricto a 61 que figuran en sus valores de registro.}
asegura: {El segundo elemento de la tupla de res para un integrante, si la cantidad de salas de las que sali´o es mayor a
0: es el promedio de salas con tiempo mayor estricto a 0 y menor estricto a 61 que figuran en sus valores de registro; sino
es 0.0.}
}'''
# de la lista de los tiempos, len(lista) es la cantidad de salas
#promedio de los tiempos de salida con 60min. 


def calcular_promedio(lista_valores: list[int]) -> float:
    sumar: int = 0
    cantidad_valores_validos: int = 0

    for valor in lista_valores:
        if valor < 61:
            sumar += valor
            cantidad_valores_validos += 1
    return (sumar/cantidad_valores_validos)

def calcular_salas_validas(lista_valores: list[int]) -> int:
    cantidad_valores_validos: int = 0

    for valor in lista_valores:
        if valor < 61:
            cantidad_valores_validos += 1
    return cantidad_valores_validos

#acá tengo que crear un nuevo diccionario con clave "nombre" y valor (len(valor_diccionario_anterior),promedio)
def promedio_de_salidas(registro: dict[str,list[int]]) -> dict[str, tuple[int,float]]:

    lista_lista_valores: list[list[float]] = list(registro.values())
    lista_nombres: list[str] = list(registro.keys())
    nuevo_diccionario: dict[str,tuple[int,float]] = {}

    for indice in range(len(lista_nombres)):
        for indice_2 in range(len(lista_lista_valores)):
            if indice_2 == indice:
                nuevo_diccionario[lista_nombres[indice]] = (
                    calcular_salas_validas(lista_lista_valores[indice_2]), calcular_promedio(lista_lista_valores[indice_2])
                )
    return nuevo_diccionario