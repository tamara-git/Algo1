'''problema cantidad de apariciones (in nombre archivo: seq⟨Char⟩, in palabra: seq⟨Char⟩) : Z {
requiere: {nombre archivo es el path con el nombre de un archivo existente y accesible}
requiere: {palabra no es vac´ıa}
asegura: {res es la cantidad de veces que palabra aparece en el archivo indicado por nombre archivo}
}'''

from typing import TextIO

#["hola como estas","yo bien y vos"]
def cadena_a_lista_palabras(linea: str) -> list[str]:
    lista_de_palabras: list[str] = []   
    palabra: str = ""
    for caracter in linea:
        if caracter != ' ' and caracter != "\n":
            palabra = palabra + caracter
        else:
            lista_de_palabras = lista_de_palabras + [palabra]
            palabra = "" 

    return lista_de_palabras


def cantidad_de_apariciones(nombre_archivo: str, palabra:str) -> int:
    archivo = open(nombre_archivo, "r", encoding= "utf-8")
    lista_lineas: list[str] = archivo.readlines()
    
    while len(lista_lineas) != 0:
        linea: str = lista_lineas.pop(0)
        if palabra in cadena_a_lista_palabras(linea):
            cantidad_apariciones += 1
            archivo.close()
    return cantidad_apariciones


    

