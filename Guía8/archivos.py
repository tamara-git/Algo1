#ejercicio 19

'''1. problema contar lineas (in nombre archivo: seq⟨Char⟩) : Z {
requiere: {nombre archivo es el path con el nombre de un archivo existente y accesible}
asegura: {res es igual a la cantidad de l´ıneas que contiene el archivo indicado por nombre archivo}
}'''

from typing import TextIO

def contar_lineas(nombre_archivo: str) -> int:
    archivo: TextIO = open(nombre_archivo,"r")
    lineas: list[str] = archivo.readlines()
    archivo.close()
    res = len(lineas) 
    return res

'''2. problema existe palabra (in nombre archivo: seq⟨Char⟩, in palabra: seq⟨Char⟩) : Bool {
requiere: {nombre archivo es el path con el nombre de un archivo existente y accesible}
requiere: {palabra no es vac´ıa}
asegura: {res es verdadero si y solo si palabra aparece al menos una vez en el archivo indicado por nombre archivo}
}'''

def existe_palabra(nombre_archivo: str, palabra: str) -> bool:
    res: bool = False
    archivo: TextIO = open(nombre_archivo, "r")
    lineas: list[str] = archivo.readlines()
    for i in range(len(lineas)):
        if palabra in lineas[i]:
            res = True
    archivo.close()
    return res

'''3. problema cantidad de apariciones (in nombre archivo: seq⟨Char⟩, in palabra: seq⟨Char⟩) : Z {
requiere: {nombre archivo es el path con el nombre de un archivo existente y accesible}
requiere: {palabra no es vac´ıa}
asegura: {res es la cantidad de veces que palabra aparece en el archivo indicado por nombre archivo}
}'''


def separar_linea_en_palabras(linea:str) -> list[str]:
    res: list[int] = []
    palabra: str = ""
    for i in range(len(linea)):
        if linea[i] != " ":
            palabra += linea[i]
        else:
            if palabra != "":
                res.append(palabra)
                palabra = ""

    res.append(palabra)
    return res
print(separar_linea_en_palabras("hola como estas locura    bien"))

def cantidad_de_apariciones(nombre_archivo: str, palabra: str) -> int:
    archivo: TextIO = open(nombre_archivo,"r")
    lineas: list[str] = archivo.readlines()
    cantidad: int= 0
    for i in range(len((lineas))):
        lista_linea: list[str] = separar_linea_en_palabras(lineas[i])
        for j in range(len(lista_linea)):
            if palabra == lista_linea[j]:
                cantidad += 1
    archivo.close()
    return cantidad

'''Ejercicio 20. Implementar una soluci´on para el siguiente problema.
problema agrupar por longitud (in nombre archivo: seq⟨Char⟩) : Diccionario⟨Z, Z⟩ {
requiere: {nombre archivo es el path con el nombre de un archivo existente y accesible}
asegura: {Para cada longitud n tal que existe al menos una palabra de longitud n en el archivo indicado por nombre archivo,
res[n] es igual a la cantidad de palabras de esa longitud}
asegura: {No hay otras claves en res que no correspondan a longitudes de palabras presentes en el archivo}
}
Por ejemplo, el diccionario
{
1: 2 ,
2: 10 ,
5: 4
}
indica que se encontraron 2 palabras de longitud 1, 10 palabras de longitud 2 y 4 palabras de longitud 5. Para este ejercicio
se consideran como palabras todas aquellas secuencias de caracteres delimitadas por espacios en blanco.
'''



'''22.problema clonar sin comentarios (in nombre archivo entrada: seq⟨Char⟩, in nombre archivo salida: seq⟨Char⟩) {
requiere: {nombre archivo entrada es el path con el nombre de un archivo existente y accesible}
requiere: {nombre archivo salida es el path con el nombre de un archivo que, si existe, se puede modificar, y si no
existe, se puede crear}
asegura: {El archivo indicado por nombre archivo salida contiene las mismas l´ıneas y en el mismo orden que el archivo
nombre archivo entrada, excepto aquellas que comienzan con el car´acter #}
}
'''
    
def clonar_sin_comentario(nombre_archivo_entrada: str, nombre_archivo_salida: str) -> None:
    archivo_entrada : TextIO = open(nombre_archivo_entrada, "r")
    archivo_salida: TextIO = open(nombre_archivo_salida, "w")
    lineas: list[int] = archivo_entrada.readlines()

    for i in range(len(lineas)):
        linea_palabras: list[str] = separar_linea_en_palabras(lineas[i]) 
        if linea_palabras[0][0] != "#":
            archivo_salida.write(lineas[i])
    archivo_entrada.close()
    archivo_salida.close()   

    
'''Ejercicio 23. problema invertir lineas (in nombre archivo entrada: seq⟨Char⟩, in nombre archivo salida: seq⟨Char⟩ ) {
requiere: {nombre archivo entrada es el path de un archivo de texto existente y accesible}
requiere: {nombre archivo salida es el path con el nombre de un archivo que, si existe, se puede modificar, y si no
existe, se puede crear}
asegura: {El archivo indicado por nombre archivo salida contiene las mismas l´ıneas que el archivo nombre archivo entrada,
pero en orden inverso}
}
Por ejemplo, si el archivo contiene lo siguiente:
Esta es la primera linea .
Y esta es la segunda .
debe generar:
Y esta es la segunda .
Esta es la primera linea .
'''

def invertir_lineas(nombre_archivo_entrada:str, nombre_archivo_salida: str) -> None:
    archivo_entrada: TextIO = open(nombre_archivo_entrada,"r")
    archivo_salida: TextIO = open(nombre_archivo_salida,"w")

    lineas: list[str] = archivo_entrada.readlines()
    archivo_salida.write(lineas[len(lineas)-1] + "\n")
    for i in range(len(lineas)-2,-1,-1):
        archivo_salida.write(lineas[i])
    archivo_entrada.close()
    archivo_salida.close()
    
