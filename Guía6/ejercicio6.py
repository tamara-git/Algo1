#Implementar todas las funciones con while

'''1. Escribir una función que imprima los números del 1 al 10.'''

def del_uno_al_diez() -> None:
    numero: int = 1
    while numero <= 10:
        print (numero)
        numero = numero + 1

del_uno_al_diez()

'''2.Escribir una función que imprima los números pares entre el 10 y el 40'''
def pares_entre_10_40() -> None:
    numero: int = 10
    while numero <= 40:
        if numero % 2 == 0:
            print(numero)
            numero = numero + 2

    

pares_entre_10_40()

'''Escribir una función que imprima la palabra "eco" 10 veces.'''
def eco() -> None:
    i: int = 1
    while i <= 10:
        print("eco")
        i = i + 1

eco()

'''Escribir una función de cuenta regresiva para lanzar un cohete. Dicha función irá imprimiendo desde el número que me
pasan por parámetro (que será positivo) hasta el 1, y por último "Despegue". '''

def cuenta_regresiva(numero:int) -> None:
    while numero >= 1:
        print(numero)
        numero = numero -1
    print("Despegue!")

cuenta_regresiva(5)

'''Hacer una función que monitoree un viaje en el tiempo. Dicha función recibe dos parámetros, "el año de partida" y
"algún año de llegada", siendo este último parámetro siempre más chico que el primero. El viaje se realizará de a saltos
de un año y la función debe mostrar el texto: "Viajó un año al pasado, estamos en el año: <año>" cada vez que se
realice un salto de año'''

def viaje_en_el_tiempo(año_de_partida:int, año_de_llegada:int) -> None:
     año:int = año_de_partida
     while año > año_de_llegada:
         año = año - 1
         print("Viajó un año al pasado, estamos en el año " + str(año))
    

viaje_en_el_tiempo(2000, 1998)

'''Implementar de nuevo la función de monitoreo de viaje en el tiempo, pero desde el año de partida hasta lo más cercano
al 384 a.C., donde conoceremos a Aristóteles. Y para que sea más rápido el viaje, ¡vamos a viajar de a 20 años en cada
salto!'''

def viaje_en_el_tiempo_2(año_de_partida:int, año_de_llegada:int) -> None:
    año:int = año_de_partida
    while (año + 20) < año_de_llegada:
        año = año + 20
        print("Viajó 20 años al pasado, estamos en el año " + str(año))
    print("Viajó " + str(año_de_llegada - año) + " año/s más al pasado, estamos en el año " + str(año_de_llegada))
    

viaje_en_el_tiempo_2(384, 2010)