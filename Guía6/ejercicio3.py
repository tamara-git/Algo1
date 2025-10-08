'''1. alguno_es_0(numero1, numero2): dados dos números racionales, decide si alguno de los dos es igual a 0.'''
def alguno_es_0(numero1: float, numero2: float) -> bool:
    return ((numero1 == 0) or (numero2 == 0))

print(alguno_es_0(0,0))

'''2. ambos_son_0(numero1, numero2): dados dos números racionales, decide si ambos son iguales a 0.'''
def ambos_son_0(numero1: float, numero2: float) -> bool:
    return (numero1 == 0 and numero2 ==0)

print(ambos_son_0(0,0))

'''3. problema es_nombre_largo (in nombre: String) : Bool {
requiere: { True }
asegura: {(res = true) ↔ (3 ≤ |nombre| ≤ 8)}
}'''

def problema_es_nombre_largo(nombre: str) -> bool:
    return (3 <= len(nombre) <= 8)

print(problema_es_nombre_largo("Brunilda"))

'''4. es_bisiesto(año): que indica si un año tiene 366 días. Recordar que un año es bisiesto si es múltiplo de 400, o bien
es múltiplo de 4 pero no de 100'''
def es_bisiesto(anio: int) -> bool:
    return (anio % 400 == 0) or (anio % 4 == 0 and anio % 100 != 100)

print(es_bisiesto(2024))