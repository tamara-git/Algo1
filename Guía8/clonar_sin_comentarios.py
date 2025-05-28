'''problema clonar sin comentarios (in nombre archivo entrada: seq⟨Char⟩, in nombre archivo salida: seq⟨Char⟩) {
requiere: {nombre archivo entrada es el path con el nombre de un archivo existente y accesible}
requiere: {nombre archivo salida es el path con el nombre de un archivo que, si existe, se puede modificar, y si no
existe, se puede crear}
asegura: {El archivo indicado por nombre archivo salida contiene las mismas l´ıneas y en el mismo orden que el archivo
nombre archivo entrada, excepto aquellas que comienzan con el car´acter #}
}
Para este ejercicio vamos a considerar que una l´ınea es un comentario si tiene un ‘#’como primer car´acter de la l´ınea, o si no
es el primer car´acter, se cumple que todos los anteriores son espacios.'''

from typing import TextIO

def es_comentario(linea:str) -> bool:
     if linea[0] == "#":
          return True
     else:
          return False

def clonar_sin_comentarios(nombre_archivo_entrada:list[str],nombre_archivo_salida:list[str]) -> None:
        archivo_entrada: TextIO = open(nombre_archivo_entrada,"r",encoding="utf-8")
        archivo_salida: TextIO = open(nombre_archivo_salida,"w",encoding="utf-8")

        lineas: list[str] = archivo_entrada.readlines()

        archivo_entrada.close()

        for linea in lineas:
            if not es_comentario(linea):
                 archivo_salida.write(linea)

        archivo_salida.close()

def sin_espacios(cadena:str) -> str:
    nueva:str = ""
    encontre_caracter : bool = False

    for caracter in cadena:
        if caracter != " ":
            encontre_caracter = True
          
        if encontre_caracter:
             
        
    

