'''
Bingo: un cart´on de bingo contiene 12 n´umeros al azar en el rango [0, 99]. Implementar una soluci´on para cada
uno de los siguientes problemas.

1. problema armar secuencia de bingo () : Cola[Z] {

requiere: {True}
asegura: {res solo contiene 100 n´umeros del 0 al 99 inclusive, sin repetidos}
asegura: {Los n´umeros de res est´an ordenados al azar}
}
Para generar n´umeros pseudoaleatorios pueden usar la funci´on random.randint(< desde >, < hasta >) que devuelve un
n´umero en el rango indicado. Recuerden importar el m´odulo random con import random.'''

from queue import Queue as Cola
import random

def armar_secuencia_de_bingo() -> Cola[int]:
    lista_sin_repetidos: list[int] = []
    bolillero: Cola[int] = Cola()
    for _ in range(100):
        numero: int = random.randint(0,99)
        if numero not in lista_sin_repetidos:
            bolillero.put(numero)
    return bolillero


'''2. problema jugar carton de bingo (in carton: seq⟨Z⟩, in bolillero: Cola[Z]) : Z {
requiere: {carton solo contiene 12 n´umeros, sin repetidos, con valores entre 0 y 99, ambos inclusive}
requiere: {bolillero solo contiene 100 n´umeros, ordenados al azar, del 0 al 99, ambos inclusive, sin repetidos}
asegura: {res es la cantidad m´ınima de jugadas necesarias para que todos los n´umeros del carton hayan salido del
bolillero}
}'''


def jugar_carton_de_bingo(carton: list[int], bolillero: Cola[int]) -> int:
    bolillero_aux: Cola[int] = Cola()
    carton_copia: list[int] = carton.copy()
    res: int = 0
    while not len(carton_copia) == 0:
        elemento: int = bolillero.get()
        bolillero_aux.put(elemento)
        if elemento in carton_copia:
            carton_copia.remove(elemento)
            res += 1
        else:
            res += 1
    
    while not bolillero_aux.empty():
        elemento: int = bolillero_aux.get()
        bolillero.put(elemento)
    return res

        

    