'''problema actualizar stock (inout inventario: Diccionario ⟨ seq⟨Char⟩, Diccionario⟨ seq⟨Char⟩, T ⟩⟩, in nombre: seq⟨Char⟩,
in cantidad: R) {
requiere: {T ∈ [Z, R]}
requiere: {cantidad ≥ 0}
requiere: {nombre es una clave existente en el inventario}
requiere: {Ninguno de los Strings de los par´ametros es vacío}
asegura: {Todos los pares clave-valor de inventario@pre están tal cual en inventario, con excepción del que tiene
como clave nombre}
asegura: {Todos los pares clave-valor de inventario están en inventario@pre}
asegura: {En inventario, el valor asociado a la clave nombre, tendrá el mismo precio que antes y la cantidad será
cantidad}
}'''

def actualizar_stock(inventario: dict[str, dict[str, float | int]], nombre: str, cantidad: float) -> None:
    
    if nombre in inventario.keys():
        inventario[nombre] = {
        "cantidad": cantidad
        }