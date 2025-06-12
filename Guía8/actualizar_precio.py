'''problema actualizar precio (inout inventario: Diccionario⟨ seq⟨Char⟩, Diccionario⟨ seq⟨Char⟩, T ⟩⟩, in nombre:seq⟨Char⟩,
in precio: R) {
requiere: {T ∈ [Z, R]}
requiere: {precio ≥ 0}
requiere: {nombre es una clave existente en el inventario}
requiere: {Ninguno de los Strings de los par´ametros es vac´ıo}
asegura: {Todos los pares clave-valor de inventario@pre est´an tal cual en inventario, con excepci´on del valor que
tiene como clave nombre}
asegura: {Todos los pares clave-valor de inventario est´an en inventario@pre}
asegura: {En inventario el diccionario asociado a nombre, tendr´a la misma cantidad que antes y el precio será precio}
}'''

def actualizar_precio(inventario: dict[str, dict[str, float | int]], nombre: str, precio: float) -> None:
    if nombre in inventario.keys():
        inventario[nombre]["precio"] = precio