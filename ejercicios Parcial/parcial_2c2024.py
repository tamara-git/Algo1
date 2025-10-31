 #Ejercicio 1 (2,25 puntos)
# Implementar la función subsecuencia_mas_larga especificada (todos_consecutivos no es testeado)

# problema subsecuencia_mas_larga (in v: seq⟨Z⟩) : ZxZ {
#   requiere: { La longitud de v es distinto de 0 }
#   asegura: { Sea x la primera subsecuencia más larga en v tal que vale todos_consecutivos(x), 
# la primera componente de res es igual a |x| y la segunda es igual al índice en v donde comenzaría x }
# }
# problema todos_consecutivos (in v: seq⟨Z⟩) : Bool {
#   asegura: { res == True <==> cada par de elementos adyacentes en v son números consecutivos, es decir, que su diferencia
#  es igual a 1 }
# }

def todos_consecutivos(v: list[int]) -> bool:
    res: bool = True
    for i in range(len(v)-1):
        if (v[i] - v[i+1] != 1) and (v[i+1] - v[i] != 1):
            res = False
    return res

def subsecuencia_mas_larga(v: list[int]) -> tuple[int,int]:
    longitud: int = 1
    longitud_max: int = 0
    indice_actual: int = 0
    indice_maximo: int = 0
    for i in range(len(v)-1):
        if (v[i] - v[i+1] == 1) or (v[i+1] - v[i] == 1):
            longitud += 1
        else:
            if longitud_max < longitud:
                longitud_max = longitud 
                indice_maximo = indice_actual
                indice_actual = i+1
                longitud = 1  
            else: 
                longitud = 1
                indice_actual = i+1
    if longitud_max < longitud:
        longitud_max = longitud
        indice_maximo = indice_actual  
    res: tuple[int,int] = (longitud_max, indice_maximo)  
    return res
           
print(subsecuencia_mas_larga([1,2,4,3,1,2,4,2,3,1,2,3,4,5,6,7,8,9]))

'''# Ejercicio 2 (2,25 puntos)
# Ana tiene exámenes de respuesta Verdadero ó Falso. Ella sabe que en cada examen la cantidad 
# de respuestas correctas cuyo valor es Falso es igual a la cantidad de respuestas correctas 
# cuyo valor es Verdadero. Tenemos el historial de las respuestas de cada exámen dados por Ana 
# en una cola. En cada uno Ana respondió todas las preguntas.

# problema mejor_resultado_de_ana (in examenes: Cola⟨ seq⟨Bool⟩ ⟩) : seq⟨Z⟩ {
#   requiere:{ Cada elemento de examenes es no vacío y tiene longitud par }
#   asegura: { res tiene la misma cantidad de elementos que examenes }
#   asegura: { res[i] es igual a la máxima cantidad de respuestas correctas que Ana podría haber respondido en el i-ésimo exámen resuelto en examenes, para 0 <= i < cantidad de elementos de examenes }
# }'''
from queue import Queue as Cola
def mejor_resultado_de_ana(examenes: Cola[list[bool]]) -> list[int]:
    res: list[int] = []
    cola_aux: Cola[list[bool]] = Cola()
    while not examenes.empty():
        examen: list[bool] = examenes.get()
        cola_aux.put(examen)
        cant_True: int = 0 
        cant_False: int = 0
        respuestas_correctas: int = len(examen)
        for i in range(len(examen)):
            if examen[i] == True:
                cant_True += 1
            else:
                cant_False += 1
        if cant_False > cant_True:
            respuestas_correctas = respuestas_correctas - (cant_False - int(respuestas_correctas/2))
        if cant_True > cant_False:
            respuestas_correctas = respuestas_correctas - (cant_True - int(respuestas_correctas/2))
        res.append(respuestas_correctas)


    return res




        
# Ejercicio 4 (2,25 puntos)
# Tenemos un texto que contiene palabras. Por simplicidad, las palabras están separadas únicamente por uno o más espacios.

# problema palabras_por_vocales (in texto: string): Diccionario⟨Z,Z⟩ {
#   requiere: { Si existe una letra vocal en texto, esta no lleva tildes, diéresis, ni ningún otro símbolo }
#   asegura: { Si existe una palabra en texto con x vocales en total, x es clave de res }
#   asegura: { Las claves de res representan la cantidad total de vocales de una palabra, y
#   cada valor corresponde a la cantidad de palabras en texto con ese número de vocales. }
#   asegura: { Los valores de res son positivos }
# }


def lista_de_palabras(secuencia: str) -> list[str]:
    palabra: str = ""
    res: list[int] = []
    for i in range(len(secuencia)):
        if secuencia[i] != " ":
            palabra += secuencia[i]
        else:
            if palabra != "":
                res.append(palabra)
                palabra = ""
    if palabra != "":
        res.append(palabra)
    return res
                

def vocales_por_palabra_en_texto(texto: str) -> list[int]:
    lista_con_vocales_por_palabra: list[int] = []
    lista_palabras_texto: list[int] = lista_de_palabras(texto)
    for i in range(len(lista_palabras_texto)):
        cantidad_vocales_palabra: int = 0
        palabra: str = lista_palabras_texto[i]
        for j in range(len(palabra)):
            letra: str = palabra[j]
            if letra in "aeiou" or letra in "AEIOU": 
                cantidad_vocales_palabra += 1        
        lista_con_vocales_por_palabra.append(cantidad_vocales_palabra)
    return lista_con_vocales_por_palabra

def vocales_en_palabra(palabra: str) -> int:
    cantidad_vocales: int = 0
    for i in range(len(palabra)):
        if palabra[i] in "aeiou" or palabra[i] in "AEIOU": 
            cantidad_vocales += 1        
    return cantidad_vocales

def palabras_con_cantidad_vocales(texto: str, cantidad_vocales: int) -> int:
    lista_palabras_texto: list[int] = lista_de_palabras(texto)
    cantidad_palabras: int = 0
    for i in range(len(lista_palabras_texto)):
        palabra: str = lista_palabras_texto[i]
        if vocales_en_palabra(palabra) == cantidad_vocales:
            cantidad_palabras += 1
    return cantidad_palabras
    

def palabras_por_vocales(texto:str) -> dict[int,int]:
    res: dict[int,int] = {}
    cantidad_vocales_por_palabra: list[int] = vocales_por_palabra_en_texto(texto)
    for i in range(len(cantidad_vocales_por_palabra)):
        cantidad: int = cantidad_vocales_por_palabra[i]
        if cantidad not in res.keys():
            res[cantidad] = palabras_con_cantidad_vocales(texto,cantidad)
    return res
