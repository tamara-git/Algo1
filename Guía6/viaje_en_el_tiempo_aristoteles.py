#Implementar de nuevo la función de monitoreo de viaje en el tiempo, pero desde el año de partida hasta lo más cercano
# al 384 a.C., donde conoceremos a Aristóteles. Y para que sea más rápido el viaje, ¡vamos a viajar de a 20 años en cada salto!

def viaje_en_el_tiempo_aristoteles(año_de_partida:int,año_de_llegada:int) -> str:
    i = año_de_partida 
    while i != año_de_llegada - 20:
        print(i)
        i -= 20
        print("Viajó 20 años al pasado, estamos en el año:", i - 20 ) 

viaje_en_el_tiempo_aristoteles(400, 384)