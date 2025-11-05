
def acomodar(s: list[str]) -> list[str]:
    res: list[str] = []
    lista_aux: list[str] = []
    for i in range(len(s)):
        if s[i] == "UP":
            res.append(s[i])
        else:
            lista_aux.append(s[i])
    
    for i in range(len(lista_aux)):
        partido: str = lista_aux[i]
        res.append(partido)

    return res 


def pos_umbral(s: list[int], u: int) -> int:
    res: int = -1
    indice_donde_supera: list[int] = []
    cantidad: int = 0
    for i in range(len(s)):
        if s[i] >= 0 and cantidad < u:
            cantidad += s[i]
        else:
            if cantidad > u:
                indice_donde_supera += [i-1]
    if len(indice_donde_supera) > 0:            
        res = indice_donde_supera.pop(0)
    return res


# 3) Columnas repetidas [3 puntos]
# Implementar la función columnas_repetidas, que dada una matriz no vacía de m
# columnas (con m par y m ≥ 2) devuelve True si las primeras m/2 columnas son
# iguales que las últimas m/2 columnas. Definimos a una secuencia de secuencias
# como matriz si todos los elementos de la primera secuencia tienen la misma
# longitud.

# problema columnas_repetidas(in mat:seq<seq<Z>>) : Bool {
#     requiere: {|mat| > 0}
#     requiere: {todos los elementos de mat tienen igual longitud m, con m > 0
#     (los elementos de mat son secuencias)}
#     requiere: {todos los elementos de mat tienen longitud par (la cantidad de
#     columnas de la matriz es par)}
#     asegura: {(res = true) <=> las primeras m/2 columnas de mat son iguales a
#     las últimas m/2 columnas}
# }

# Por ejemplo, dada la matriz
#m = [[1,2,1,2],
#     [-5,6,-5,6],
#      [0,1,0,1]]

# se debería devolver res = true
# TIP: para dividir un número entero x por 2 y obtener como resultado un número
# entero puede utilizarse la siguiente instrucción: int(x/2)

def columna(mat: list[list[int]], col: int) -> list[int]:
    secuencia: list[int] = []
    for fila in range(len(mat)):
        secuencia.append(mat[fila][col])
    return secuencia

def armo_matriz_dividida(mat: list[list[int]], desde: int, hasta:int) -> list[list[int]]:
    res: list[list[int]] = []
    for i in range(desde,hasta+1):
        res.append(columna(mat,i))
    return res 

def mitades_iguales(mitad1: list[list[int]], mitad2: list[list[int]]) -> bool:
    res: int = True 
    if mitad1 != mitad2:
        res = False
    return res 

def columnas_repetidas(mat: list[list[int]]) -> bool:
    col: int = len(mat[0])
    mitad1: list[list[int]] = armo_matriz_dividida(mat, 0, int(col/2)-1)
    mitad2: list[list[int]] = armo_matriz_dividida(mat, int(col/2),col-1) 
    return mitades_iguales(mitad1,mitad2)


# 4) Rugby 4 naciones [3 puntos]
# Desde hace más de 10 años existe en el mundo del rugby un torneo que disputan
# anualmente 4 selecciones del sur global (Argentina, Australia, Nueva Zelanda y
# Sudáfrica). Este torneo se llama "The rugby championship" o comunmente "4
# naciones", ya que suplantó al viejo "3 naciones".

# Implementar la función cuenta_posiciones_por_nacion que dada la lista de
# naciones que compiten en el torneo, y el diccionario que tiene los resultados
# de los torneos anuales en el formato año:posiciones_naciones, donde año es un
# número entero y posiciones_naciones es una lista de strings con los nombres de
# las naciones, genere un diccionario de naciones:#posiciones, que para cada
# Nación devuelva la lista de cuántas veces salió en esa posición.

# Tip: para crear una lista con tantos ceros como naciones se puede utilizar la
# siguiente sintaxis lista_ceros = [0]*len(naciones)

# problema cuenta_posiciones_por_nacion(in naciones: seq<String>, in torneos:
# dict<Z,seq<String>>: dict<String,seq<Z>> {
#     requiere: {naciones no tiene elementos repetidos}
#     requiere: {Los valores del diccionario torneos son permutaciones de la
#     lista naciones (es decir, tienen exactamente los mismos elementos que
#     naciones, en cualquier orden posible)}
#     asegura: {res tiene como claves los elementos de naciones}
#     asegura: {El valor en res de una nación es una lista de |naciones|
#     elementos que indica en la posición i cuántas veces salió esa nación en la
#     i-ésima posición.}
# }
# Por ejemplo, dados
# naciones= ["arg", "aus", "nz", "sud"]
# torneos= {2023:["nz", "sud", "arg", "aus"], 2022:["nz", "sud", "aus", "arg"]}
# se debería devolver res = {"arg": [0,0,1,1], "aus": [0,0,1,1], "nz": [2,0,0,0],
# "sud": [0,2,0,0]}

def posicion_en_torneo(torneos: dict[int,list[str]], pais: str) -> list[int]:
    res: list[int] = []
    for año in torneos.keys():
        paises: list[str] = torneos[año]
        if len(res) == 0:
            for i in range(len(paises)):
                if paises[i] != pais:
                    res.append(0)
                else: 
                    res.append(1)
        else:
            for i in range(len(paises)):
                if paises[i] == pais:
                    res[i] += 1
    return res
        
                        

def cuenta_posiciones_por_nacion(naciones: list[str], torneos: dict[int, list[str]]) -> dict[str,list[int]]:
    res: dict[str,list[int]] = {}
    for i in range(len(naciones)):
        res[naciones[i]] = posicion_en_torneo(torneos, naciones[i])

    return res

