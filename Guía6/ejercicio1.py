from math import sqrt, pi

''' 1. problema imprimir_hola_mundo () {
requiere: { True }
asegura: { imprime “¡Hola mundo!"por consola}
}'''

#Tengo que aclarar que no devuelve nada en el tipo.
#Si uso el print adentro de la función no hace falta poner print (imprimir_hola_mundo ()) al final del código.


def imprimir_hola_mundo() -> None:
    print("¡Hola mundo!")

imprimir_hola_mundo()

'''2. imprimir_un_verso(): que imprima un verso de una canción que vos elijas, respetando los saltos de 
línea mediante el caracter \n'''

def imprimir_un_verso() -> None:
    print("De aquel amor\nDe música ligera\nNada nos libra\nNada más queda")

imprimir_un_verso()

'''3. raizDe2(): que devuelva la raíz cuadrada de 2 con 4 decimales. Ver función round'''

def raizDe2() -> None:
    print(round(sqrt(2), 4))

raizDe2()

'''4. factorial_de_dos()
problema factorial_2 () : Z {
requiere: { True }
asegura: {res = 2!}
}
'''
def factorial_2() -> int:
    res: int = 2
    return res 

print(factorial_2())

'''5. perimetro: que devuelva el perímetro de la circunferencia de radio 1. Utilizar la biblioteca math
 mediante el comando
import math y la constante math.pi
problema perimetro () : R {
requiere: { T rue }
asegura: {res = 2 × π }
}'''

def perimetro () -> float:
    res: float = 2*pi 
    return res 

print(perimetro()) 
