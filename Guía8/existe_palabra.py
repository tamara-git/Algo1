'''problema existe palabra (in nombre archivo: seq⟨Char⟩, in palabra: seq⟨Char⟩) : Bool {
requiere: {nombre archivo es el path con el nombre de un archivo existente y accesible}
requiere: {palabra no es vacía}
asegura: {res es verdadero si y solo si palabra aparece al menos una vez en el archivo indicado por nombre archivo}
}'''

from typing import TextIO

#["hola como estas","yo bien y vos"]
def cadena_a_lista_palabras(linea: str) -> list[str]:
    lista_de_palabras: list[str] = []   
    palabra: str = ""
    for caracter in linea:
        if caracter != ' ' or caracter != "\n":
            palabra = palabra + caracter
        else:
            lista_de_palabras = lista_de_palabras + [palabra]
            palabra = "" 

    return lista_de_palabras

print(cadena_a_lista_palabras("hola como estas"))

def existe_palabra(nombre_archivo: str, palabra: str) -> bool:
    archivo: TextIO = open(nombre_archivo, "r", encoding = "utf-8")

    lista_lineas: list[str] =  archivo.readlines()
    while len(lista_lineas) != 0:
        linea: str = lista_lineas.pop(0)
        if palabra in cadena_a_lista_palabras(linea):
            archivo.close()
            return True
        return False