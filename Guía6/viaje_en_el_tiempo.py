#Hacer una función que monitoree un viaje en el tiempo. Dicha función recibe dos parámetros, “el año de partida” y
# “algún año de llegada”, siendo este último parámetro siempre más chico que el primero. El viaje se realizará de a saltos
# de un año y la función debe mostrar el texto: “Viajó un año al pasado, estamos en el año: <año>” cada vez que se
# realice un salto de año.

def viaje_en_el_tiempo(año_de_partida:int,año_de_llegada:int) -> str:
    while año_de_partida != año_de_llegada:
        año_de_partida -= 1
        print("Viajó un año al pasado, estamos en el año:", año_de_partida ) 

viaje_en_el_tiempo(1990,1980)

