'''1. problema pertenece a cada uno version 1 (in s:seq⟨seq⟨Z⟩⟩, in e:Z, out res: seq⟨Bool⟩) {
requiere: { T rue }
asegura: { |res| ≥ |s| }
asegura: { Para todo i ∈ Z si 0 ≤ i < |s| → (res[i] = true ↔ pertenece(s[i], e)) }
}
Nota: Reutilizar la funci´on pertenece() implementada previamente para listas.'''

def pertenece(s: list[int], e: int) -> bool:
    res = False
    for elem in s:
        if elem == e:
            res = True
    return res

def pertenece_a_cada_uno_version_1(secuencia: list[list[int]], elemento: int) -> list[bool]:
    res: list[bool] = []
    for i in range(len(secuencia)): 
        if pertenece(secuencia[i], elemento) == True:
            res.append(True)
        else:
            res.append(False)
    return res


print(pertenece_a_cada_uno_version_1([[1,2,3,4],[5,6,7,8],[1,2,3,4,5]],5))

'''1. problema es matriz (in s:seq⟨seq⟨Z⟩⟩) : Bool {
requiere: { T rue }
asegura: { res = true ↔ (|s| > 0) ∧ (|s[0]| > 0) ∧ (Para todo i ∈ Z si 0 ≤ i < |s| → |s[i]| = |s[0]|) }
}
'''
def es_matriz(matriz: list[list[int]]) -> bool:
    res: bool = False 
    columna: int = len(matriz[0])
    for i in range(len(matriz)):
        if len(matriz[i]) == columna:
            res = True 
        else:
            res = False 
    return res

print(es_matriz([[1,2,3],[1,24,4],[1,2,3]]))

'''2. problema filas ordenadas (in m:seq⟨seq⟨Z⟩⟩, out res: seq⟨Bool⟩) {
requiere: { esM atriz(m) }
asegura: { Para todo i ∈ Z si 0 ≤ i < |res| → (res[i] = true ↔ ordenados(s[i])) }
}
Nota: Reutilizar la funci´on ordenados() implementada previamente para listas'''

def ordenados(secuencia:list[int]) -> bool:
    res: bool = True
    for i in range(len(secuencia)-1):
        if secuencia[i] > secuencia[i+1]:
            res = False  
    return res

print(ordenados([1,10,3,3,7,8,9]))


def filas_ordenadas(matriz: list[list[int]]) -> list[bool]:
    res: list[bool] = []
    for i in range(len(matriz)):
        if ordenados(matriz[i]) == True:
            res.append(True)
        else:
            res.append(False)
    return res

'''3. problema columna (in m:seq⟨seq⟨Z⟩⟩, in c: Z) : seq⟨Z⟩ {
requiere: { esM atriz(m) }
requiere: { c < |m[0]| }
requiere: { c ≥ 0 }
asegura: { Devuelve una secuencia con exactamente los mismos elementos de la columna c de la matriz m, en
el mismo orden que aparecen }
}
'''

def columna(matriz:list[list[int]], columna: int) -> list[int]:
    secuencia: list[int] = []
    for i in range(len(matriz)):
        secuencia.append(matriz[i][columna])
    return secuencia

print(columna([[1,2,3,4],[5,6,7,8],[9,10,11,12],[0,0,0,0]], 2))
        


'''4. problema columnas ordenadas (in m:seq⟨seq⟨Z⟩⟩) : seq⟨Bool⟩ {
requiere: { esM atriz(m) }
asegura: { Para todo ´ındice de columna c: 0 ≤ c < |m[0]| → (res[c] = true ↔ ordenados(columna(m, c))) }
asegura: {|res| = |m[0]|}
}
Nota: Reutilizar la funci´on ordenados() implementada previamente para listas'''

def columnas_ordenadas(matriz: list[list[int]]) -> list[bool]:
    res: list[bool] = []
    columna: list[int] = []
    for i in range(len(matriz[0])):
        for j in range(len(matriz)):
            columna.append(matriz[j][i])
        if ordenados(columna) == True:
            res.append(True)
        else:
            res.append(False)
        columna = []
    return res


print(columnas_ordenadas([[1,0,3,4],[5,6,7,8],[9,10,1,12],[10,20,0,90]]))


'''5. problema transponer (in m:seq⟨seq⟨Z⟩⟩) : seq⟨seq⟨Z⟩⟩ {
requiere: { esM atriz(m) }
asegura: { Devuelve mt
(o sea la matriz transpuesta) }
}
Nota: Usar columna() para ir obteniendo todas las columnas de la matriz.'''
    
def transponer(matriz: list[list[int]]) -> list[list[int]]:
    transpuesta: list[list[int]] = []
    for i in range(len(matriz[0])):
        transpuesta.append(columna(matriz,i))
    return transpuesta

print(transponer([[1,2,3],
                 [4,5,6],[7,8,9],[10,11,12]]))


'''6. Ta-Te-Ti Tradicional:
problema quien gana tateti (in m:seq⟨seq⟨Char⟩⟩) : Z {
requiere: { esMatriz(m) }
requiere: { |m| = 3 }
requiere: { |m[0]| = 3 }
requiere: { En la matriz si hay 3 X alineadas verticalmente =⇒ no hay 3 O alineadas verticalmente }
requiere: { En la matriz si hay 3 O alineadas verticalmente =⇒ no hay 3 X alineadas verticalmente }
requiere: { En la matriz si hay 3 X alineadas horizontalmente =⇒ no hay 3 O alineadas horizontalmente }
requiere: { En la matriz si hay 3 O alineadas horizontalmente =⇒ no hay 3 X alineadas horizontalmente }
requiere: { Para todo i,j ∈ {0, 1, 2} =⇒ m[i][j] = X ∨ m[i][j] = O ∨ m[i][j] = ” ”}
asegura: { Si hay 3 O alineadas verticalmente, horizontalmente o en diagonal, devuelve 0 }
asegura: { Si hay 3 X alineadas verticalmente, horizontalmente o en diagonal, devuelve 1 }
asegura: { Si no hay ni 3 X, ni 3 O alineadas verticalmente, horizontalmente o en diagonal, devuelve 2 }'''

def diagonal(matriz:list[list[str]]) -> list[str]:
    sec_diagonal: list[str] = []
    for i in range(len(matriz[0])):
        sec_diagonal.append(matriz[i][i])
    return sec_diagonal

def diagonal_inversa(matriz:list[list[str]]) -> list[str]:
    sec_diagonal: list[str] = []
    for i in range(len(matriz[0])):
        sec_diagonal.append(matriz[i][len(matriz[0])-1-i])
    return sec_diagonal

def gana_horizontal(tateti:list[list[str]]) -> int:
    res: int = 2
    for fila in range(len(tateti)):
        if tateti[fila] == ["O","O","O"] or tateti[fila] == ["X","X","X"]:
            if tateti[fila] == ["O","O","O"]:
                res = 0
            else: 
                res = 1
    return res


def gana_vertical(tateti:list[list[str]]) -> int:
    res: int = 2
    for i in range(len(tateti[0])):
        if columna(tateti,i) == ["O","O","O"] or columna(tateti,i) == ["X","X","X"]:
            if columna(tateti,i) == ["O","O","O"]:
                res = 0
            else:
                res = 1 
    return res


def gana_diagonal(tateti:list[list[str]]) -> int:
    res: int = 0
    if diagonal(tateti) == ["O","O","O"] or diagonal_inversa(tateti) == ["O","O","O"]:
        res = 0
    elif diagonal(tateti) == ["X","X","X"] or diagonal_inversa(tateti) == ["X","X","X"]:
        res = 1 
    else:
        res = 2
    return res

def quien_gana_tateti(tateti:list[list[str]]) -> int:
    res: int = 0
    if gana_horizontal(tateti) != 2:
        res = gana_horizontal(tateti)
    elif gana_vertical(tateti) != 2:
        res = gana_vertical(tateti)
    elif gana_diagonal(tateti) != 2:
        res = gana_diagonal(tateti)
    else:
        res = 2
    return res

print(quien_gana_tateti([["O","X","O"],
                         ["X","O","X"],
                         ["O","O","X"]]))






