'''Vamos a representar un hospital con una matriz en donde las filas son los pisos, y las
columnas son las camas. Los valores de la matriz son Booleanos que indican si la cama
est´a ocupada o no. Si el valor es verdadero (True) indica que la cama est´a ocupada.
problema nivel de ocupacion (in camas por piso:seq⟨seq⟨Bool⟩⟩) : seq⟨R⟩ {
requiere: {Todos los pisos tienen la misma cantidad de camas.}
requiere: {Hay por lo menos 1 piso en el hospital.}
requiere: {Hay por lo menos una cama por piso.}
asegura: {|res| es igual a la cantidad de pisos del hospital.}
asegura: {Para todo 0 ≤ i < |res| se cumple que res[i] es igual a la cantidad de
camas ocupadas del piso i dividido el total de camas del piso i).}
}'''

def nivel_de_ocupacion(camas_por_piso: list[list[bool]]) -> list[float]:

    camas_ocupadas: int = 0
    camas_totales : int = len(camas_totales[0])
    res: list[float] = []
    for fila in range(len(camas_por_piso)):
        for columna in range(len(camas_por_piso[0])):
            if camas_por_piso[fila][columna] == True:
                camas_ocupadas += 1
        res.append(camas_ocupadas/camas_totales)
    return res
