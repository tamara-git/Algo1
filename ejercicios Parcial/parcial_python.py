'''problema cantidad_parejas_que_suman (in s: seq⟨Z⟩, in n: Z) : Z {
requiere: { - }
asegura: { res es la cantidad de parejas s[i] y s[j] de números de s tales que s[i] + s[j] = n (con i < j) }
}
Ejemplo: cantidad_parejas_que_suman([1,3,2,5,4,8], 5) debe devolver 2'''

def cantidad_parejas_que_suman(s: list[int], n: int) -> int:
    cantidad: int = 0
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if s[i] + s[j] == n:
                cantidad += 1
            
    return cantidad

print(cantidad_parejas_que_suman([1,3,2,5,4,8,-3], 5))


'''En un supermercado tenemos una fila de clientes esperando para ser atendidos por algún cajero. Cada cliente tiene un nombre, un método de pago y una cantidad de productos. La fila de clientes se representa como
una Cola de String x String x Z, donde el primer elemento es el nombre del cliente, el segundo es el método de pago y el tercero es la cantidad de productos. Implementar la función pasar_por_autoservicio:
Nota: los métodos de pago son strings conformados por letras minúsculas.
problema pasar_por_autoservicio (inout clientes: Cola⟨ String x String x Z ⟩) : String'''

from queue import Queue as Cola
def pasar_por_autoservicio(clientes: Cola[tuple[str,str,int]]) -> str:
    cola_aux: Cola[tuple[str,str,int]] = Cola()
    cantidad: int = 0
    res: str = ""
    testeo: list[tuple[str,str,int]] = []
    while not clientes.empty():
        datos_cliente:  tuple[str,str,int] = clientes.get()
        if datos_cliente[1] != "efectivo" and datos_cliente[2] <= 15 and cantidad < 1:
            res = datos_cliente[0] 
            cantidad += 1
        else:
            cola_aux.put(datos_cliente)
            testeo.append(datos_cliente)

    while not cola_aux.empty():
        datos_cliente: tuple[str,str,int] = cola_aux.get()
        clientes.put(datos_cliente)

    return res


def pasar_por_autoservicio_testeo_len(clientes: Cola[tuple[str,str,int]]) -> str:
    cola_aux: Cola[tuple[str,str,int]] = Cola()
    cantidad: int = 0
    res: str = ""
    testeo: list[tuple[str,str,int]] = []
    while not clientes.empty():
        datos_cliente:  tuple[str,str,int] = clientes.get()
        if datos_cliente[1] != "efectivo" and datos_cliente[2] <= 15 and cantidad < 1:
            res = datos_cliente[0] 
            cantidad += 1
        else:
            cola_aux.put(datos_cliente)
            testeo.append(datos_cliente)

    while not cola_aux.empty():
        datos_cliente: tuple[str,str,int] = cola_aux.get()
        clientes.put(datos_cliente)

    return testeo


'''requiere:{ Las primeras componentes de clientes son strings no vacíos y todos distintos entre sí }
requiere:{ Las terceras componentes de clientes son números positivos }
requiere:{ Existe al menos un elemento c dentro de la cola clientes tal que c1
 ≠ "efectivo" y c2
 ≤ 15 }
modifica: { clientes }
asegura: { Sea c el primer elemento insertado en la cola clientes tal que c1
 ≠ "efectivo" y c2
 ≤ 15, entonces res = c0
 }
asegura: { clientes contiene todos los elementos de clientes@pre excepto la tupla que contiene a res en su primera posición, en el mismo orden que en clientes@pre. }
}
Ejemplo: pasar_por_autoservicio(clientes) debe devolver "Bruno" (y quitar su tupla de la cola)
si clientes es una cola en la cual se insertaron (en orden) los siguientes elementos:
1. ("Ana", "efectivo", 13)
2. ("Juan", "qr", 22)
3. ("Bruno", "tarjeta", 14)'''

''' Ejercicio 3 [2,5 puntos]
Implementar la función intercambiar_e_invertir_columnas:
problema intercambiar_e_invertir_columnas(inout A: seq⟨seq⟨Z⟩⟩, in col1: Z, in col2: Z) {
requiere: { Todas las filas de A tienen la misma longitud (estrictamente positiva)}
requiere: { |A| > 0}
requiere: { 0 ≤ col1 < |A[0]| }
requiere: { 0 ≤ col2 < |A[0]| }
requiere: { col1 ≠ col2 }
modifica: { A }
asegura: { A tiene exactamente las mismas dimensiones que A@pre }
asegura: { A[i][j] = A@pre[i][j] para todo i, j en rango tal que j ≠ col1 y j ≠ col2 }
asegura: { A[i][col1] = A@pre[|A|-1-i][col2] para todo i tal que 0 ≤ i < |A| }
asegura: { A[i][col2] = A@pre[|A|-1-i][col1] para todo i tal que 0 ≤ i < |A| }
}
Ejemplo: Si mat = [[1,2,3],
                   [40,50,60], 
                   [-7,-8,-9]], luego de ejecutarse
intercambiar_e_invertir_columnas(mat,1,2)
 debería ocurrir que print(mat) muestre [[1, -9, -8],
                                         [40, 60, 50], 
                                         [-7, 3, 2]]'''

def devolver_columna(A:list[list[int]], col: int) -> list[int]:
    columna: list[int] = []
    for i in range(len(A)):
        columna.append(A[i][col])
    return columna


def invertir_columna(A:list[list[int]], col: int) -> list[int]:
    columna: list[int] = devolver_columna(A,col) 
    columna_invertida: list[int] = []
    for i in range(len(columna)-1,-1,-1):
        columna_invertida.append(columna[i])
    return columna_invertida


def reemplazar_columnas_invertidas_en_matriz(A:list[list[int]], col1: int, col2: int) -> None:
    columna_invertida_1: list[int] = invertir_columna(A,col1)
    columna_invertida_2: list[int] = invertir_columna(A,col2)
    for i in range(len(A)):
        A[i][col1] = columna_invertida_1[i]
        A[i][col2] = columna_invertida_2[i]


def intercambiar_columnas(A:list[list[int]], col1: int, col2:int) -> None:
    columna_col1 : list[int] = devolver_columna(A,col1)
    columna_col2: list[int] = devolver_columna(A,col2)
    for i in range(len(A)):
        A[i][col1] = columna_col2[i]
        A[i][col2] = columna_col1[i]


def intercambiar_e_invertir_columnas(A: list[list[int]], col1: int, col2: int) -> None:
    intercambiar_columnas(A, col1, col2)
    reemplazar_columnas_invertidas_en_matriz(A,col1,col2)

'''Se realizaron dos censos en los cuales se le preguntó a cada persona en que localidad vive. Estos datos fueron almacenados en dos diccionarios cuyas claves son los nombres de las personas, y sus valores las
localidades en las cuales viven. Implementar la función mantuvieron_residencia:
problema mantuvieron_residencia (in censo1: Diccionario⟨String,String⟩, in censo2: Diccionario⟨String,String⟩): Diccionario⟨String,Z⟩ {
requiere: { Las claves de censo1 son las mismas que las claves de censo2 }
asegura: { k es clave de res si y sólo si existe alguna clave p en censo1 tal que al obtener su valor tanto en censo1 como en censo2, este es igual a k }
asegura: { El valor de cada clave de res representa la cantidad de personas que en ambos censos vivía en esa localidad, es decir, que mantuvieron su residencia en la misma localidad entre ambos censos }
}
Ejemplo: mantuvieron_residencia({'Juan': 'Merlo', 'Ana': 'Merlo'}, {'Juan': 'Castelar', 'Ana': 'Merlo'})
debe devolver {'Merlo': 1}'''

def mantuvieron_residencia(censo1: dict[str,str], censo2: dict[str,str]) -> dict[str,int]:
    res: dict[str,int] = {}
    cantidad_existente: int = 0
    nueva_cantidad: int = 0
    for nombre in censo1.keys():
        if censo1[nombre] == censo2[nombre]:
            if censo1[nombre] in res:
                cantidad_existente += 1
                res[censo1[nombre]] = cantidad_existente
            else: 
                nueva_cantidad += 1
                cantidad_existente = nueva_cantidad 
                res[censo1[nombre]] = nueva_cantidad
                nueva_cantidad = 0

    return res
    
            


