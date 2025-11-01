'''problema prefijo_que_mas_suma (in s: seq<Z>) : Z {
  requiere: { |s| > 0 }
  asegura: { res = ∑ ki=0 s[i] para algún k tal que 0 ≤ k < |s| }
  asegura: { res ≥ ∑ ki=0 s[i] para todos los k tales que 0 ≤ k < |s| }
}
'''

def prefijo_que_mas_suma(s: list[int]) -> int:
    sumaEnPrefijo: int = s[0]
    prefijo: int = 0
    for i in range(1,len(s)):
        if s[i] + sumaEnPrefijo > sumaEnPrefijo:
            sumaEnPrefijo = s[i] + sumaEnPrefijo
            prefijo += 1
    return prefijo

print(prefijo_que_mas_suma([-100,2,3,5,3,0]))

'''problema primera_entrega_en_blanco (in examenes: Pila< String x Z >) : String {
  requiere: { Las primeras componentes de examenes son strings no vacíos y todos distintos entre sí }
  requiere: { Existe al menos un elemento p dentro de la pila examenes tal que p1=0 }
  asegura: { Sea p el primer elemento insertado en la pila examenes tal que p1=0. Entonces, res = p0 }
}
'''
from queue import LifoQueue as Pila

def copiar_pila(pila: Pila[tuple[str,int]]) -> Pila[tuple[str,int]]:
    pila_copia: Pila[tuple[str,int]] = Pila()
    pila_aux: Pila[tuple[str,int]] = Pila()

    while not pila.empty():
        elemento: tuple[str,int] = pila.get()
        pila_aux.put(elemento)
    
    while not pila_aux.empty():
        elemento: tuple[str,int] = pila_aux.get()
        pila_copia.put(elemento)
        pila.put(elemento)

    return pila_copia


def primera_entrega_en_blanco(examenes: Pila[tuple[str,int]]) -> str:
    examenes_copia: Pila[tuple[str,int]] = copiar_pila(examenes)
    res: str = ""
    while not examenes_copia.empty():
        examen: tuple[str,int] = examenes_copia.get()
        if examen[1] == 0:
            res = examen[0]
    return res


'''problema desplazar_columna_hacia_arriba(inout A: seq< seq<Z > >, in col: Z) {
  requiere: { Todas las filas de A tienen la misma longitud (estrictamente positiva) }
  requiere: { |A| > 0 }
  requiere: { 0 ≤ col < |A[0]| }
  modifica: { A }
  asegura: { A tiene exactamente las mismas dimensiones que A@pre }
  asegura: { A[i][j] = A@pre[i][j] para todo i, j en rango tal que col ≠ j }
  asegura: { A[i][col] = A@pre[i+1][col] para todo i tal que 0 ≤ i < |A|-1 }
  asegura: { A[|A|-1][col] = A@pre[0][col] }
}
'''
def columna(A: list[list[int]], col: int) -> list[int]:
    res: list[int] = []
    for i in range(len(A)):
        elemento: int = A[i][col]
        res.append(elemento)
    return res 

def desplazar_secuencia(lista: list[int]) -> list[int]:
    res: list[int] = []
    for i in range(1,len(lista)):
        res.append(lista[i])
    res.append(lista[0])
    return res


def desplazar_columna_hacia_arriba(A: list[list[int]], col: int) -> None:
    columna_desplazada: list[int] = desplazar_secuencia(columna(A,col))
    for i in range(len(A)):
        A[i][col] = columna_desplazada[i]

'''problema armar_ranking (in podios: seq[Diccionario[Z, String]]): Diccionario[String, Z] {
  requiere: { Cada diccionario de podios tiene como claves los valores 1, 2 y 3 (o algún subconjunto de los mismos) }
  requiere: { Sea d un diccionario en la secuencia podios, entonces d no contiene valores repetidos }
  asegura: { nom es clave de res si y sólo si existe un diccionario en podios tal que nom es valor de dicho diccionario }
  asegura: { Cada clave c de res tiene como valor la sumatoria de los puntos obtenidos por c en cada una de las competencias de podios (suma 3 puntos si salió primero, 2 puntos si salió segundo, 1 punto si salió tercero y 0 puntos si no estuvo en el podio de esa competencia) }
}
'''

def armar_ranking(podios: list[dict[int,str]]) -> dict[str,int]:
    res: dict[str,int] = {}
    for i in range(len(podios)):
        competencia: dict[int,str] = podios[i]
        for puesto in competencia.keys():
            ganador: str = competencia[puesto]
            if ganador not in res:
                res[ganador] = puesto
            else:
                res[ganador] += puesto
    return res

