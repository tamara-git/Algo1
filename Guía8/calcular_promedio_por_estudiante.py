'''problema calcular promedio por estudiante (in notas: seq⟨seq⟨Char⟩ × R⟩) : Diccionario ⟨ seq⟨Char⟩, R⟩ {
requiere: {El primer componente de las tuplas de notas no es una cadena vac´ıa}
requiere: {El segundo componente de las tuplas de notas est´a en el rango [0, 10]}
asegura: {Todas las claves de res son nombres que aparecen en notas (primer componente)}
asegura: {Todos los nombres de notas (primer componente) son clave en res}
asegura: {El valor de cada clave de res es el promedio de todas las notas que obtuvo el estudiante (segunda componente
de notas)}
}'''

#[("luis",10).("luis",6),("fede",10)]
def calcular_promedio_por_estudiante(notas:(list[tuple[str,float]])) -> dict[str,float]:
    suma_notas : dict[str,float] = {}
    cantidad_notas : dict[str,int] = {}

    for estudiante, nota in notas:
        if estudiante not in suma_notas.keys():
            suma_notas[estudiante] = nota
            cantidad_notas[estudiante] = 1
        else:
             suma_notas[estudiante] += nota
             cantidad_notas[estudiante] += 1

    promedios: dict[str, float] = {}
    for estudiante in suma_notas.keys():
        promedios[estudiante] = suma_notas[estudiante] / cantidad_notas[estudiante]

        return promedios
