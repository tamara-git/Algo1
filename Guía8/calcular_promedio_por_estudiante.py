'''problema calcular promedio por estudiante (in notas: seq⟨seq⟨Char⟩ × R⟩) : Diccionario ⟨ seq⟨Char⟩, R⟩ {
requiere: {El primer componente de las tuplas de notas no es una cadena vac´ıa}
requiere: {El segundo componente de las tuplas de notas est´a en el rango [0, 10]}
asegura: {Todas las claves de res son nombres que aparecen en notas (primer componente)}
asegura: {Todos los nombres de notas (primer componente) son clave en res}
asegura: {El valor de cada clave de res es el promedio de todas las notas que obtuvo el estudiante (segunda componente
de notas)}
}'''

#[("luis",10).("luis",6),("fede",10)]
def calcular_promedio_de_estudiante(calificaciones: list[tuple[str, float]], estudiante: str) -> float:
    suma_notas: float = 0.0
    cantidad_notas: int = 0
    
    for calificación in calificaciones:
        calificante: str = calificación[0]
        nota: float = calificación[1]
        
        if calificante == estudiante:
            suma_notas += nota
            cantidad_notas += 1
    
    if cantidad_notas == 0: return 0.0
    return suma_notas / cantidad_notas


def calcular_promedio_por_estudiante(calificaciones: list[tuple[str, float]]) -> dict[str, float]:
    notas: dict[str, float] = {}
    
    for calificación in calificaciones:
        estudiante: str = calificación[0]
        
        if estudiante not in notas.keys():
            promedio: float = calcular_promedio_de_estudiante(calificaciones, estudiante)
            notas[estudiante] = promedio
    
    return notas