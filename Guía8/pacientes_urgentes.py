'''Vamos a modelar una guardia de un hospital usando una cola donde se van almacenando los pedidos de atenci´on
para los pacientes que van llegando. A cada paciente se le asigna una prioridad del 1 al 10 (donde la prioridad 1 es la m´as urgente
y requiere atenci´on inmediata) junto con su nombre y la especialidad m´edica que le corresponde. Implementar una soluci´on para
el siguiente problema.
problema pacientes urgentes (in c:Cola[Z× seq⟨Char⟩ × seq⟨Char⟩]) : Z {
requiere: {Todos los elementos de c tienen como primer componente de la tupla un entero positivo y menor a 11}
asegura: {res es la cantidad de elementos de c que tienen como primer componente de la tupla un n´umero menor a 4}
}'''

from queue import Queue as Cola
# devuelve la cantidad de pacientes de la cola que son prioridad menor a 4.

def copiar_cola(cola:Cola[tuple[int,str,str]]) -> Cola[tuple[int,str,str]]:
    cola_copia: Cola[tuple[int,str,str]] = Cola()
    cola_auxiliar: Cola[tuple[int,str,str]] = Cola()

    while not cola.empty():
        elemento: tuple[int,str,str] = cola.get()
        cola_auxiliar.put(elemento)

    while not cola_auxiliar.empty():
        elemento: tuple[int,str,str] = cola_auxiliar.get()
        cola.put(elemento)
        cola_copia.put(elemento)

    return cola_copia



def pacientes_urgentes(c: Cola[tuple[int,str,str]]) -> int:
    c_copia: Cola[tuple[int,str,str]] = copiar_cola(c)
    contador: int = 0
    while not c_copia.empty():
        datos: tuple[int,str,str] = c_copia.get()
        for indice in range(len(datos)):
            if indice == 0 and datos[indice] < 4:
                contador += 1

    return contador