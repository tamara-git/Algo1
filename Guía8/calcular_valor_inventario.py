'''problema calcular valor inventario (in inventario: Diccionario ⟨ seq⟨Char⟩, Diccionario ⟨ seq⟨Char⟩, T ⟩⟩) : R {
requiere: {T ∈ [Z, R]}
requiere: {Ninguno de los Strings del inventario es vac´ıo}
asegura: {res es la suma, para cada producto, del precio multiplicado por la cantidad}
}
'''

def calcular_valor_inventario(inventario: dict[str, dict[str, float | int]]) -> float:
    suma_valores: float = 0.0
    for nombre in inventario.keys():
        res = inventario[nombre]["precio"] * inventario[nombre]["cantidad"]
        suma_valores += res
    return suma_valores