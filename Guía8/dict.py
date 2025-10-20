'''3. Diccionarios
En esta secci´on trabajaremos con el tipo dict de Python, que nos permite asociar claves con valores.
Ejercicio 16. Implementar una soluci´on para el siguiente problema.
problema calcular promedio por estudiante (in notas: seq⟨seq⟨Char⟩ × R⟩) : Diccionario ⟨ seq⟨Char⟩, R⟩ {
requiere: {El primer componente de las tuplas de notas no es una cadena vac´ıa}
requiere: {El segundo componente de las tuplas de notas est´a en el rango [0, 10]}
asegura: {Todas las claves de res son nombres que aparecen en notas (primer componente)}
asegura: {Todos los nombres de notas (primer componente) son clave en res}
asegura: {El valor de cada clave de res es el promedio de todas las notas que obtuvo el estudiante (segundo componente
de notas)}
}
Cada nota de la lista recibida como par´ametro es una tupla que tiene como primer componente el nombre del estudiante y,
como segundo, la nota que se sac´o en un examen.
Por ejemplo:
notas: list[tuple[str, float]] = [("Sole", 9.5), ("Maxi", 8.0), ("Sole", 9.0)]
calcular promedio por estudiante(notas) debe devolver {"Sole": 9.25, "Maxi": 8.0}'''

def promedio_estudiante(notas: list[tuple[str,float]], estudiante: str) -> int:
    promedio: int = 0
    suma_total: int = 0
    cantidad: int = 0
    for i in range(len(notas)):
        estudiante_actual: str = notas[i][0]
        nota_actual: float = notas[i][1]
        if estudiante_actual == estudiante:
            suma_total += nota_actual
            cantidad += 1
    promedio = suma_total/cantidad
    return promedio


def calcular_promedio_por_estudiante(notas: list[tuple[str,float]]) -> dict[str,float]:
    res: dict[str,float] = {}
    calif: int = 0
    for i in range(len(notas)):
        estudiante_actual: str = notas[i][0] 
        if estudiante_actual not in res.keys():
            res[estudiante_actual] = promedio_estudiante(notas, estudiante_actual)
    return res
        
        