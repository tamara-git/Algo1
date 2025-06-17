'''Ejercicio 9. Juego de la Gallina
El juego del gallina es una competici´on en la que dos participantes conducen un vehículo en dirección al del contrario; si
alguno se desv´ıa de la trayectoria de choque pierde y es humillado por comportarse como un ”gallina”. Se hizo un torneo para
ver qui´en es el menos gallina. Juegan todos contra todos una vez y van sumando puntos, o restando. Si dos jugadores juegan y
se chocan entre s´ı, entonces pierde cada uno 5 puntos por haberse da˜nado. Si ambos jugadores se desv´ıan, pierde cada uno 10
puntos por gallinas. Si uno no se desv´ıa y el otro s´ı, el gallina pierde 15 puntos por ser humillado y el ganador suma 10 puntos!
En este torneo, cada persona que participa tiene una estrategia predefinida para competir: o siempre se dev´ıa, o nunca lo hace.
Se debe programar la funci´on ‘torneo de gallinas’ que recibe un diccionario (donde las claves representan los nombres de los
participantes que se anotaron en el torneo, y los valores sus respectivas estrategias) y devuelve un diccionario con los puntajes
obtendidos por cada jugador.
problema torneo de gallinas (in estrategias: dict<str, str>) : dict<str, Z> {
requiere: {estrategias tiene por lo menos 2 elementos (jugadores).}
requiere: {Las claves de estrategias tienen longitud mayor a 0.}
requiere: {Los valores de estrategias s´olo pueden ser los strs ”me desv´ıo siempre” ´o ”me la banco y no me desv´ıo”.}
asegura: {Las claves de res y las claves de estrategias son iguales.}
asegura: {Para cada jugador p perteneciente a claves(estrategias), res[p] es igual a la cantidad de puntos que obtuvo al
finalizar el torneo, dado que jug´o una vez contra cada otro jugador.}
}'''

def torneo_de_gallinas(estrategias: dict[str,str]) -> dict[str,int]:
    puntaje_final: dict[str,int] = {}
    sumar: int = 0

    for jugador in estrategias.keys():
        if estrategias[jugador] == "me desvío siempre":
            for valor in estrategias.values(): 
                if valor != estrategias[jugador]:
                    if valor == "me desvío siempre":
                        sumar += (-10)
            
                if valor == "me la banco y no me devío":
                     sumar += (-15)
        puntaje_final[jugador] = sumar

        if estrategias[jugador] == "me la banco y no me devío":
            for valor in estrategias.values(): 
                if valor != estrategias[jugador]:
                    if valor == "me desvío siempre":
                        sumar += 10
                    if valor == "me la banco y no me devío":
                        sumar += 5
        puntaje_final[jugador] = sumar

    return puntaje_final