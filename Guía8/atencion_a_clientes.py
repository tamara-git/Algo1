'''
La gerencia de un banco nos pide modelar la atención de los clientes usando una cola donde se van registrando
los pedidos de atención. Cada vez que ingresa una persona a la entidad, debe completar sus datos en una pantalla que está a la
entrada: Nombre y Apellido, DNI, tipo de cuenta (true si es preferencial o false en el caso contrario) y si tiene prioridad (true
o false) por ser adulto +65, embarazada o con movilidad reducida.
La atención a los clientes se da por el siguiente orden: primero las personas que tienen prioridad, luego las que tienen cuenta
bancaria preferencial y por último el resto. Dentro de cada subgrupo de clientes, se respeta el orden de llegada.
1. Dar una especificación para el problema planteado.
2. Implementar atencion a clientes(in c : Cola[tuple[str, int, bool, bool]]) → Cola[tuple[str, int, bool, bool]] que dada la cola 
de ingreso de clientes al banco devuelve la cola en la que van a ser atendidos.
'''

from queue import Queue as Cola  

def copiar_cola(cola: Cola[tuple[str, int, bool, bool]]) -> Cola[tuple[str, int, bool, bool]]:
    cola_copia: Cola[tuple[str, int, bool, bool]] = Cola()
    cola_auxiliar: Cola[tuple[str, int, bool, bool]] = Cola()

    while not cola.empty():
        elemento_tupla: tuple[str, int, bool, bool] = cola.get()
        cola_auxiliar.put(elemento_tupla)

    while not cola_auxiliar.empty():
        elemento_tupla: tuple[str, int, bool, bool] = cola_auxiliar.get()
        cola_copia.put(elemento_tupla)
        cola.put(elemento_tupla)

    return cola_copia


# Voy a crear tres colas, una de prioridad, una de cuenta preferencial y otra normal.
# Se respeta el orden de llegada.
# Luego pongo todo en una sola cola.
def atencion_a_clientes(c: Cola[tuple[str, int, bool, bool]]) ->  Cola[tuple[str, int, bool, bool]]:
    c_copia: Cola[tuple[str, int, bool, bool]] = copiar_cola(c)
    cola_prioridad: Cola[tuple[str, int, bool, bool]] = Cola()
    cola_preferencial: Cola[tuple[str, int, bool, bool]] = Cola()
    cola_comun: Cola[tuple[str, int, bool, bool]] = Cola()
    cola_ordenada: Cola[tuple[str, int, bool, bool]] = Cola()
    
    while not c_copia.empty():
        datos: tuple[str, int, bool, bool] = c_copia.get()
        for indice in range(len(datos)):
            if indice == 2 and datos[indice] == True:
                cola_prioridad.put(datos)
            if indice == 3 and datos[indice] == True:
                cola_preferencial.put(datos)
            else:
                cola_comun.put(datos)
        
    while not cola_prioridad.empty():
        datos: tuple[str, int, bool, bool] = cola_prioridad.get()
        cola_ordenada.put(datos)

    while not cola_preferencial.empty():
        datos: tuple[str, int, bool, bool] = cola_preferencial.get()
        cola_ordenada.put(datos)

    while not cola_comun.empty():
        datos: tuple[str, int, bool, bool] = cola_comun.get()
        cola_ordenada.put(datos)

    return cola_ordenada


def son_colas_iguales(c1: Cola[tuple[str, int, bool, bool]], c2: Cola[tuple[str, int, bool, bool]]) -> bool:
    c1_copia: Cola[tuple[str, int, bool, bool]] = copiar_cola(c1)
    c2_copia: Cola[tuple[str, int, bool, bool]] = copiar_cola(c2)
    lista_c1: list[tuple[str, int, bool, bool]] = []
    lista_c2: list[tuple[str, int, bool, bool]] = []

    while not c1_copia.empty():
        datos_c1: tuple[str, int, bool, bool] = c1_copia.get()
        lista_c1 = lista_c1.append(datos_c1)
        
    while not c2_copia.empty():
        datos_c2: tuple[str, int, bool, bool] = c2_copia.get()
        lista_c2 = lista_c2.append(datos_c2)

    
    for indice in range(len(lista_c1)):
        if lista_c1[indice] != lista_c2[indice] and len(lista_c1) != len(lista_c2):
            return False
    return True

