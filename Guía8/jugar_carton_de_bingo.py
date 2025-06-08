'''problema jugar carton de bingo (in carton: seq⟨Z⟩, in bolillero: Cola[Z]) : Z {
requiere: {carton solo contiene 12 números, sin repetidos, con valores entre 0 y 99, ambos inclusive}
requiere: {bolillero solo contiene 100 números, ordenados al azar, del 0 al 99, ambos inclusive, sin repetidos}
asegura: {res es la cantidad mínima de jugadas necesarias para que todos los números del carton hayan salido del
bolillero}
}'''

from queue import Queue as Cola

def eliminar_numero(lista: list[int], numero: int) -> list[int]:
    lista_sin_el_numero: list[int] = []

    for elemento in lista:
        if elemento == numero:
            lista_sin_el_numero += []
        else:
            lista_sin_el_numero += [elemento]

    return lista_sin_el_numero
            

def jugar_carton_de_bingo(carton: list[int], bolillero: Cola[int]) -> int:
    cantidad_jugadas: int = 0
    carton_copia: list[int] = carton.copy()

    while len(carton_copia) != 0:
        numero: int = bolillero.get()
        if numero in carton_copia:
            carton_copia = eliminar_numero(carton_copia, numero)
            cantidad_jugadas += 1
        else: 
            cantidad_jugadas += 1
        
    return cantidad_jugadas 