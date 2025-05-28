'''Ejercicio 19. Implementar una soluci´on para cada uno de los siguientes problemas.
1. problema contar lineas (in nombre archivo: seq⟨Char⟩) : Z {
requiere: {nombre archivo es el path con el nombre de un archivo existente y accesible}
asegura: {res es igual a la cantidad de l´ıneas que contiene el archivo indicado por nombre archivo}
}'''

from typing import TextIO

def contar_lineas(nombre_archivo: str) -> int:
    archivo: TextIO = open(nombre_archivo,"r",encoding="utf-8")
    res:int = len(archivo.readlines())
    archivo.close()

    return res
