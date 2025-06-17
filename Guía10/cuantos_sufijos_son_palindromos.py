'''Ejercicio 11. Sufijos que son pal´ındromos
Decimos que una palabra es pal´ındromo si se lee igual de izquierda a derecha que de derecha a izquierda. Se nos pide programar
en python la siguiente funci´on:
problema cuantos sufijos son palindromos (in texto: str) : Z {
requiere: {True}
asegura: {res es igual a la cantidad de pal´ındromos que hay en el conjunto de sufijos de texto.}
}
Nota: un sufijo es una subsecuencia de texto que va desde una posici´on cualquiera hasta el al final de la palabra. Ej: ”Diego”,
el conjunto de sufijos es: ”Diego”, ”iego”,”ego”,”go”, ”o”. Para este ejercicio no consideraremos a ”” como sufijo de ning´un texto.
'''
# ejemplos: loco,  Málaga,  mapa, Diego, Jesús 

def conjuntos_de_sufijos(texto: str) -> list[str]: 
   
    conjunto_sufijos: list[str] = []
    variable: int = 0

    conjunto_sufijos.append(texto)
    while variable < len(texto):
        variable += 1
        sufijo: str = ""
        for indice_2 in range(variable, len(texto)): 
            sufijo += texto[indice_2]
        conjunto_sufijos.append(sufijo)
    conjunto_sufijos.pop()
    return conjunto_sufijos


def es_palindromo(texto: str) -> bool:
    palabra_inversa: str = ""

    for indice in range(len(texto) -1, -1, -1):
        palabra_inversa += texto[indice]

    if palabra_inversa != texto:
        return False
    return True


def cuantos_sufijos_son_palindromos(texto: str) -> int:
    contador: int = 0
    
    for sufijo in conjuntos_de_sufijos(texto):
        if es_palindromo(sufijo):
            contador += 1
    return contador
