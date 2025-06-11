'''Se debe desarrollar un sistema de gestión de inventario para una tienda de ropa. Este sistema debe permitir llevar
un registro de los productos en el inventario y realizar operaciones como agregar nuevos productos, actualizar las existencias y
calcular el valor total del inventario.
Para resolver este problema vamos a utilizar un dict llamado inventario que almacenará la info de los
productos. En este dict, cada clave será el nombre de un producto, y su valor asociado será otro dict con los
atributos del producto. Este segundo dict tendrá 2 claves posibles: 'precio' y 'cantidad', cuyos valores serán de tipo float
e int, respectivamente.
Un ejemplo de inventario, con un solo producto, es: {“remera”: {“precio”: 999.99, “cantidad”: 3}}).

Se necesitará un dict cuyas claves son de tipo String (“precio” y “cantidad”) y cuyos valores serán de tipo float e int respectivamente.
Para declarar los tipos de este diccionario mediante anotaciones en Python, se procede de la siguiente manera:
para indicar que los valores pueden ser de + de un tipo. (representar una unión de tipos).
mi diccionario: dict[str, int | float]

1. problema agregar producto (inout inventario: Diccionario⟨ seq⟨Char⟩, Diccionario⟨ seq⟨Char⟩, T ⟩⟩, in nombre: seq⟨Char⟩,
in precio: R, in cantidad: Z) {
asegura: {Todas los pares clave-valor de inventario est´an en inventario@pre y, adem´as, hay una nueva con clave
igual a nombre y como valor tendrá un diccionario con los pares clave-valor (“precio”, precio) y (“cantidad”,
cantidad)}
}
'''
# precio: , cantidad:
def agregar_producto(inventario: dict[str, dict[ str | float]], nombre: str, precio: float, cantidad: int):


    if nombre not in inventario.keys():
        inventario[nombre] = {
            "precio": precio,
            "cantidad": cantidad
        }
    




