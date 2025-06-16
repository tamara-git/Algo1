'''. Sala de Escape - Racha m´as larga
Dada una lista con los tiempos (en minutos) registrados para cada sala de escape a la que fue una persona, escribir una
funci´on en Python que devuelva una tupla con el ´ındice de inicio y el ´ındice de fin de la subsecuencia m´as larga de salidas
exitosas de salas de escape consecutivas.
problema racha mas larga (in tiempos: seq⟨Z⟩) : <Z×Z> {
requiere: {Hay por lo menos un elemento en tiempos entre 1 y 60 inclusive.}
requiere: {Todos los tiempos en tiempos est´an entre 0 y 61 inclusive.}
asegura: {En la primera posici´on de res est´a la posici´on (´ındice de la lista) de la sala que inicia la racha m´as larga.}
asegura: {En la segunda posici´on de res est´a la posici´on (´ındice de la lista) de la sala que finaliza la racha m´as larga.}
asegura: {El elemento de la primer posici´on de res en tiempos es mayor estricto 0 y menor estricto que 61.}
asegura: {El elemento de la segunda posici´on de res en tiempos es mayor estricto 0 y menor estricto que 61.}
asegura: {La primera posici´on de res es menor o igual a la segunda posici´on de res.}
asegura: {No hay valores iguales a 0 o a 61 en tiempos entre la primer posici´on de res y la segunda posici´on de res.}
asegura: {No hay otra subsecuencia de salidas exitosas, en tiempos, de mayor longitud que la que est´a entre la primer
posici´on de res y la segunda posici´on de res.}
asegura: {Si hay dos o m´as subsecuencias de salidas exitosas de mayor longitud en tiempos, res debe contener la primera
de ellas.}
}'''

def racha_mas_larga(tiempos: list[int]) -> tuple[int,int]:
    contador: int = 1
    contador_maximo: int = 0
    lista_tiempos: list[int] = []
    tupla_maxima: tuple[int,int] = ()

    for indice in range(len(tiempos)-1):
        if tiempos[indice] not in [0,61] and tiempos[indice + 1] not in [0,61]:
            contador += 1
            lista_tiempos.append(tiempos[indice])
            if indice != 0:
                lista_tiempos.pop()
            primer_posicion: int = lista_tiempos.pop()

        else:
            if contador > contador_maximo:
                contador_maximo = contador
                lista_tiempos.append(indice - 1)
                segunda_posicion: int = lista_tiempos.pop()
                lista_tiempos = []
            (primer_posicion, segunda_posicion)
            
