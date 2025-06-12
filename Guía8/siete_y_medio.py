'''Vamos a escribir un programa para simular el juego conocido como 7 y medio. El mismo deber´a generar un n´umero
aleatorio entre 0 y 12 (excluyendo el 8 y 9) y deber´a luego preguntarle al usuario si desea seguir sacando otra “carta”
o plantarse. En este ´ultimo caso el programa debe terminar. Los n´umeros aleatorios obtenidos deber´an sumarse seg´un
el n´umero obtenido salvo por las “figuras” (10, 11 y 12) que sumar´an medio punto cada una. El programa debe ir
acumulando los valores y si se pasa de 7.5 debe informar que el usuario ha perdido. Al finalizar la funci´on devuelve
el historial de “cartas” que hizo que el usuario gane o pierda. Para generar n´umeros pseudo-aleatorios entre 1 y 12
utilizaremos la función random.randint(1,12). Al mismo tiempo, la funci´on random.choice() puede ser de gran
ayuda a la hora de repartir cartas.'''

import random
def siete_y_medio() -> None:
    sumar: float = 0.0
    lista_numeros: list[int] = []

    while True:
        respuesta = input("¿Otra carta? (escribe 'no' para terminar)")
        if respuesta == "si":
            numero: int = random.randint(1,12)
            while numero in [8,9]:
                numero = random.randint(1,12)
            if numero in [10,11,12]:
                numero = 0.5
            print(numero)
            sumar += numero
            lista_numeros += [numero]

            if sumar > 7.5:
                break
            
        if respuesta == "no":
            break
        
    while len(lista_numeros) != 0:
        numero = lista_numeros.pop(0)
        print(numero)
    print("total de cartas:", sumar)

    if sumar != 7.5:
        print("Perdiste!, fracasado")
    else:
        print("Ganaste!, fracasado")

siete_y_medio()