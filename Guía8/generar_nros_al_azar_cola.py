'''implementar una soluci´on para el siguiente problema.
problema generar nros al azar (in cantidad: Z, in desde: Z, in hasta: Z) : Cola[Z] {
requiere: {cantidad ≥ 0}
requiere: {desde ≤ hasta}
asegura: {El tama˜no de res es igual a cantidad}
asegura: {Todos los elementos de res son valores entre desde y hasta (ambos inclusive), seleccionados aleatoriamente
con probabilidad uniforme}
}
Para generar números en un rango con probabilidad uniforme, pueden usar la función random.randint(< desde >, < hasta >)
que devuelve un número en el rango indicado. Recuerden importar el módulo random con import random. Pueden usar la clase
Queue() que es un ejemplo de una implementaci´on b´asica de una Cola:
from queue import Queue as Cola # importa Queue y le asigna el alias Cola
c = Cola () # creo una cola
c . put (1) # encolo el 1
elemento = c . get () # desencolo
c . empty () # devuelve true si y solo si la cola está vacía'''

from queue import Queue as Cola
def generar_nros_al_azar(cantidad:int, desde:int, hasta:int) -> Cola[int]:
    