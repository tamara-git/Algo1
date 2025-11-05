

def ultima_aparicion(s: list[int], e: int) -> int:
    for i in range(len(s)):
        if s[i] == e:
            indice: int = i
    return indice


def pertenece_a_lista(lista: list[int], elem: int) -> bool:
    res: bool = True
    if elem not in lista:
        res = False 
    return res 

def eliminar_repetidos(lista: list[int]) -> list[int]:
    sin_repetidos: list[int] = []
    for i in range(len(lista)):
        if lista[i] not in sin_repetidos:
            sin_repetidos.append(lista[i])
    return sin_repetidos


def elementos_exclusivos(s: list[int], t: list[int]) -> list[int]:
    res: list[int] = []
    s_sin_repetidos: list[int] = eliminar_repetidos(s)
    t_sin_repetidos: list[int] = eliminar_repetidos(t)
    for i in range(len(s_sin_repetidos)):
        if not pertenece_a_lista(t_sin_repetidos, s_sin_repetidos[i]):
            res.append( s_sin_repetidos[i])
    for j in range(len(t_sin_repetidos)):
        if not pertenece_a_lista(eliminar_repetidos(s_sin_repetidos), t_sin_repetidos[j]):
            res.append(t_sin_repetidos[j])
    return res 


def contar_traducciones_iguales(ing: dict[str,str], ale: dict[str,str]) -> int:
    cantidad_palabras: int = 0
    for palabra in ing.keys():
        if palabra in ale.keys() and ale[palabra] == ing[palabra]:
            cantidad_palabras += 1
    return cantidad_palabras


def convertir_a_diccionario(lista:list[int]) -> dict[int,int]:
    res: dict[int,int] = {}
    for i in range(len(lista)):
        elemento: int = lista[i]
        res[elemento] = lista.count(elemento)
    return res 
