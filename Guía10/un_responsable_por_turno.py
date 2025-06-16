'''Veterinaria - Tabla turnos
Las personas responsables de los turnos est´an anotadas en una matriz donde las columnas representan los días, en orden de
lunes a domingo, y cada fila un rango de una hora. Hay cuatro filas para los turnos de la mañana (9, 10, 11 y 12 hs) y otras
cuatro para la tarde (14, 15, 16 y 17).

Para hacer más eficiente el trabajo del personal de una veterinaria, se necesita analizar si quienes quedan de responsables,
est´an asignadas de manera continuada en los turnos de cada día.
Para ello se pide desarrollar una funci´on en Python que, dada la matriz de turnos, devuelva una lista de tuplas de bool, una
por cada día. Cada tupla debe contener dos elementos. El primer elemento debe ser True si y solo si todos los valores de los
turnos de la ma˜nana para ese día son iguales entre sí. El segundo elemento debe ser True si y solo si todos los valores de los
turnos de la tarde para ese día son iguales entre sí.
Siempre hay una persona responsable en cualquier horario de la veterinaria.
problema un responsable por turno (in grilla horaria : seq⟨seq⟨str⟩⟩) : seq⟨Bool × Bool⟩ {
requiere: {|grilla horaria| = 8.}
requiere: {Todos los elementos de grilla horaria tienen el mismo tamaño (mayor a 0 y menor 8).}
requiere: {No hay cadenas vacías en las listas de grilla horaria.}
asegura: {|res| = |grilla horaria[0]|.}
asegura: {El primer valor de la tupla en res [i], con i:Z, 0 res| es igual a True los primeros 4 valores de la columna i de
grilla horaria son iguales entre sí.}
asegura: {El segundo valor de la tupla en res [i], con i:Z, 0 res| es igual a True los ´ultimos 4 valores de la columna i de
grilla horaria son iguales entre sí.}
}
'''
# L   M
#(9   9
# 10  10    )

# |res| = 7
#res = (bool,bool),... x7
def un_responsable_por_turno(grilla_horaria: list[list[str]]) -> list[tuple[bool, bool]]:
    res: list[tuple[bool, bool]] = []         
    tupla: tuple[bool,bool] = ()
    turno_mañana: bool = True
    turno_tarde: bool = True
    
    filas: int = len(grilla_horaria)
    columnas: int = len(grilla_horaria[0])


    for columna in range(columnas):
        for fila in range(filas-4):
            responsable_mañana: str = grilla_horaria[0][columna]
            if grilla_horaria[fila][columna] != responsable_mañana:
                turno_mañana = False 
                if turno_mañana == False:
                    break
                    
            turno_mañana = True
        
        for fila in range(filas-4, filas):
            responsable_tarde: str = grilla_horaria[4][columna]
            if grilla_horaria[fila][columna] != responsable_tarde:
                turno_tarde = False    
                if turno_tarde == False:
                    break

            turno_tarde = True    
        
        tupla = (turno_mañana, turno_tarde )


        res.append(tupla)

    return res
