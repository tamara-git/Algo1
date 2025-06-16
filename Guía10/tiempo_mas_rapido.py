'''Ejercicio 6. Sala de Escape - Tiempo m´as r´apido
Dada una lista con los tiempos (en minutos) registrados para cada sala de escape de Capital, escribir una funci´on en Python
que devuelva la posici´on (´ındice) en la cual se encuentra el tiempo m´as r´apido, excluyendo las salas en las que no haya salido (0
o mayor a 60).
problema tiempo mas rapido (in tiempos salas: seq⟨Z⟩) : Z {
requiere: {Hay por lo menos un elemento en tiempos salas entre 1 y 60 inclusive.}
requiere: {Todos los tiempos en tiempos salas est´an entre 0 y 61 inclusive.}
asegura: {res es la posici´on de la sala en tiempos salas de la que m´as r´apido se sali´o (en caso que haya m´as de una,
devolver la primera, osea la de menor índice).}
}'''

def tiempo_mas_rapido(tiempos_salas: list[int]) -> int:
    lista_indice: list[int] = []
    mayor_tiempo: int = tiempos_salas[0]

    for indice in range(len(tiempos_salas)-1):
        if tiempos_salas[indice] in [0,61]:
            continue
        if tiempos_salas[indice] > mayor_tiempo:
            mayor_tiempo = tiempos_salas[indice]
            lista_indice.append(indice)
        if tiempos_salas[indice] == mayor_tiempo:
            continue 
    return lista_indice.pop()

