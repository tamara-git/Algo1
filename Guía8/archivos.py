'''1. problema contar lineas (in nombre archivo: seq⟨Char⟩) : Z {
requiere: {nombre archivo es el path con el nombre de un archivo existente y accesible}
asegura: {res es igual a la cantidad de l´ıneas que contiene el archivo indicado por nombre archivo}
}'''

from typing import TextIO

def contar_lineas(nombre_archivo: str) -> int:
    archivo: TextIO = open("archivo_entrada.txt","r")
    lineas: list[str] = archivo.readlines()
    archivo.close()
    res = len(lineas) 




'''22.problema clonar sin comentarios (in nombre archivo entrada: seq⟨Char⟩, in nombre archivo salida: seq⟨Char⟩) {
requiere: {nombre archivo entrada es el path con el nombre de un archivo existente y accesible}
requiere: {nombre archivo salida es el path con el nombre de un archivo que, si existe, se puede modificar, y si no
existe, se puede crear}
asegura: {El archivo indicado por nombre archivo salida contiene las mismas l´ıneas y en el mismo orden que el archivo
nombre archivo entrada, excepto aquellas que comienzan con el car´acter #}
}
'''
#implementar la función archivo.split()
# " hola como estas" = ["hola","como","estas"]
#def separar_en_palabras(lineas: list[str]) -> list[str]:
    

def clonar_sin_comentario(nombre_archivo_entrada: str, nombre_archivo_salida: str) -> None:
    archivo_entrada : TextIO = open("nombre_archivo_entrada.txt", "r")
    archivo_salida: TextIO = open("nombre_archivo_salida.txt", "w")

    # lineas: list[str] = archivo_entrada.readlines()
    # for linea in lineas
        

    
