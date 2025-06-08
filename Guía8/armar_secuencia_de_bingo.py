'''Bingo: un cartón de bingo contiene 12 números al azar en el rango [0, 99]. Implementar una soluci´on para cada
uno de los siguientes problemas.
1. problema armar secuencia de bingo () : Cola[Z] {
requiere: {True}
asegura: {res solo contiene 100 números del 0 al 99 inclusive, sin repetidos}
asegura: {Los números de res est´an ordenados al azar}
}
Para generar números pseudoaleatorios pueden usar la función random.randint(< desde >, < hasta >) que devuelve un
número en el rango indicado. Recuerden importar el módulo random con import random'''

from queue import Queue as Cola
import random 

def armar_secuencia_de_bingo() -> Cola[int]:
    # Armo una lista, con los numeros, a medida que los voy metiendo en la cola, y si se repite, no va a la cola.
    bolillero: Cola[int] = Cola()
    lista_numeros: list[int] = []


    for _ in range(100):
        numero: int = random.randint(0,99)
        if numero not in lista_numeros:
            lista_numeros.append(numero)
            bolillero.put(numero)
    return bolillero

