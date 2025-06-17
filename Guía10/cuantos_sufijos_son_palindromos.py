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

def eliminar_primer_caracter(texto: str) -> str: 
    sufijo: str = ""
    for indice in range(1,len(texto)):
        sufijo += texto[indice]
    return sufijo

def es_palindromo(texto: str) -> bool:
    palabra_inversa: str = ""

    for indice in range(len(texto), -1):
        palabra_inversa += texto[indice]

    if texto != palabra_inversa:
        return False
    return True


def cuantos_sufijos_son_palindromos(texto: str) -> int:
    conjunto_sufijos: list[str] = []
    contador: int = 0

    while len(conjunto_sufijos) < len(texto):
        conjunto_sufijos.append(eliminar_primer_caracter(texto))
    
    for sufijo in conjunto_sufijos:
        if es_palindromo(sufijo):
            contador += 1
    return contador
