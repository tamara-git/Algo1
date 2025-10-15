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
    cola: Cola[int] = Cola()
    for _ in range(100):
        numero: int = random.randint(0,99)
        if numero not in lista_sin_repetidos:
            cola.put(numero)
    return cola


'''2. problema jugar carton de bingo (in carton: seq⟨Z⟩, in bolillero: Cola[Z]) : Z {
requiere: {carton solo contiene 12 n´umeros, sin repetidos, con valores entre 0 y 99, ambos inclusive}
requiere: {bolillero solo contiene 100 n´umeros, ordenados al azar, del 0 al 99, ambos inclusive, sin repetidos}
asegura: {res es la cantidad m´ınima de jugadas necesarias para que todos los n´umeros del carton hayan salido del
bolillero}
}'''


def jugar_carton_de_bingo(carton: list[int], bolillero: Cola[int]) -> int:
    carton_copia: list[int] = carton.copy()
    restablecer_bolillero: Cola[int] = Cola()
    res: int = 0
    while not carton_copia.empty():
        elemento: int = bolillero.get()
        if elemento in carton_copia:
            carton_copia.remove(elemento)
            res += 1
        else:
            res += 1
    return res
        

    