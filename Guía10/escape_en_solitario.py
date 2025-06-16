'''Ejercicio 8. Sala de Escape - Escape en solitario
Dada una matriz donde las columnas representan a cada amigo y las filas representan las salas de escape, y los valores son los
tiempos (en minutos) registrados para cada sala (0 si no fueron, 61 si no salieron, y un n´umero entre 1 y 60 si salieron), escribir
una funci´on en Python que devuelva los ´ındices de todas las filas (que representan las salas) en las cuales el primer, segundo y
cuarto amigo no fueron (0), pero el tercero s´ı fue independientemente de si sali´o o no).
problema escape en solitario (in amigos por salas: seq⟨seq⟨Z⟩⟩) : seq⟨Z⟩ {
requiere: {Hay por lo menos una sala en amigos por salas.}
requiere: {Hay 4 amigos en amigos por salas.}
requiere: {Todos los tiempos en cada sala de amigos por salas est´an entre 0 y 61 inclusive.}
asegura: {La longitud de res es menor igual que la longitud de amigos por salas.}
asegura: {Por cada sala en amigos por salas cuyo primer, segundo y cuarto valor sea 0, y el tercer valor sea distinto de
0, la posici´on de dicha sala en amigos por salas debe aparecer res.}
asegura: {Para todo i pertenciente a res se cumple que el primer, segundo y cuarto valor de amigos por salas[i] es 0, y
el tercer valor es distinto de 0.}
}
'''
"""un ejemplo:
    [0, 0, 0, 1]
    [0, 0, 3, 0]
    [40,50,1, 0]

"""

def escape_en_solitario(amigos_por_salas: list[list[int]]) -> list[int]:
   
    filas: int = len(amigos_por_salas)   #
    lista_solitario: list[int] = []
    res: bool = False

    for fila in range(filas):
        for columna in [0,1,3]:
                if amigos_por_salas[fila][columna] != 0:
                    break
        if amigos_por_salas[fila][columna] == 0:   
            lista_solitario.append(fila)
 
    return lista_solitario
                    
