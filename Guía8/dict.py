from queue import LifoQueue as Pila
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
    for i in range(len(notas)):
        estudiante_actual: str = notas[i][0] 
        if estudiante_actual not in res.keys():
            res[estudiante_actual] = promedio_estudiante(notas, estudiante_actual)
    return res

#Ejercicio 17

'''2.problema visitar sitio (inout historiales: Diccionario⟨seq⟨Char⟩, P ila[seq⟨Char⟩]⟩, in usuario: seq⟨Char⟩, in sitio: seq⟨Char⟩)
{
requiere: {Ninguno de los Strings de los par´ametros es vac´ıo}
asegura: {Si usuario es una de las claves de historiales@pre, entonces se agrega sitio a su pila de historiales@pre[usuario]}
asegura: {Si usuario no es una de las claves de historiales@pre, entonces historiales[usuario] es igual a la pila
que tiene solo el elemento sitio}
asegura: {No se modifica ning´un otro historial salvo, si existe, el de usuario}
asegura: {Todos los pares clave-valor de historiales@pre est´an en historiales}
asegura: {Todos los pares clave-valor de historiales est´an en historiales@pre, salvo historiales[usuario] que podr´ıa
no existir en historiales@pre}
}'''

def visitar_sitio(historiales: dict[str, Pila[str]], usuario:str, sitio: str) -> None:
    if usuario not in historiales:
        sitios: Pila[str] = Pila()
        sitios.put(sitio)
        historiales[usuario] =  sitios
    else:
        historiales[usuario].put(sitio)
    

'''3. problema navegar atras (inout historiales: Diccionario⟨ seq⟨Char⟩, Pila[ seq⟨Char⟩, in usuario: seq⟨Char⟩⟩) : seq⟨Char⟩
{
requiere: {Ninguno de los Strings de los par´ametros es vac´ıo}
requiere: {usuario es una clave de historiales}
requiere: {La pila asociada a usuario no est´a vac´ıa}
asegura: {res es igual al tope de historiales@pre[usuario]}
asegura: {historiales[usuario] es igual a historiales@pre[usuario] quitando el tope de la pila de
historiales@pre[usuario]}
asegura: {En historiales, salvo la pila asociada a usuario, no se modifica ning´un otro por clave-valor}
}'''

def navegar_atras(historiales: dict[str, Pila[str]], usuario: str) -> str:
    res: str = historiales[usuario].get()
    return res


#Ejercicio 18
'''1. problema agregar producto (inout inventario: Diccionario⟨ seq⟨Char⟩, Diccionario⟨ seq⟨Char⟩, T ⟩⟩, in nombre: seq⟨Char⟩,
in precio: R, in cantidad: Z) {
requiere: {T ∈ [Z, R]}
requiere: {cantidad ≥ 0}
requiere: {precio ≥ 0}
requiere: {Ninguno de los Strings de los par´ametros es vac´ıo}
requiere: {nombre no es una clave de inventario }
asegura: {Todas los pares clave-valor de inventario@pre est´an tal cual en inventario}
asegura: {Todas los pares clave-valor de inventario est´an en inventario@pre y, adem´as, hay una nueva con clave
igual a nombre y como valor tendr´a un diccionario con los pares clave-valor (“precio”, precio) y (“cantidad”,
cantidad)}
}
Se necesitar´a un diccionario cuyas claves son de tipo String (“precio” y “cantidad”) y cuyos valores ser´an de tipo float
y enteros respectivamente. Para declarar los tipos de este diccionario mediante anotaciones en Python, se procede de la
siguiente manera:

Union indica que los valores pueden ser de m´as de un tipo.
En Python 3.10 o superior:
usar el operador | para representar una uni´on de tipos.   (mi_diccionario: dict[str, int | float])
'''

def agregar_producto(inventario: dict[str, dict[str, int | float]], nombre: str, precio: float, cantidad: int) -> None:
    if nombre not in inventario.keys():
        inventario[nombre] = {"precio": precio,
                          "cantidad": cantidad}


'''2. problema actualizar stock (inout inventario: Diccionario ⟨ seq⟨Char⟩, Diccionario⟨ seq⟨Char⟩, T ⟩⟩, in nombre: seq⟨Char⟩,
in cantidad: R) {
requiere: {T ∈ [Z, R]}
requiere: {cantidad ≥ 0}
requiere: {nombre es una clave existente en el inventario}
requiere: {Ninguno de los Strings de los par´ametros es vac´ıo}
asegura: {Todos los pares clave-valor de inventario@pre est´an tal cual en inventario, con excepci´on del que tiene
como clave nombre}
asegura: {Todos los pares clave-valor de inventario est´an en inventario@pre}
asegura: {En inventario, el valor asociado a la clave nombre, tendr´a el mismo precio que antes y la cantidad ser´a
cantidad}
}
'''

def actualizar_stock(inventario: dict[str, dict[str, int|float]], nombre: str, cantidad: float) -> None:
    valor: dict[str,int|float] = inventario[nombre]
    if nombre in inventario.keys():
           valor["cantidad"] = cantidad

'''3. problema actualizar precio (inout inventario: Diccionario⟨ seq⟨Char⟩, Diccionario⟨ seq⟨Char⟩, T ⟩⟩, in nombre:seq⟨Char⟩,
in precio: R) {
requiere: {T ∈ [Z, R]}
requiere: {precio ≥ 0}
requiere: {nombre es una clave existente en el inventario}
requiere: {Ninguno de los Strings de los par´ametros es vac´ıo}
asegura: {Todos los pares clave-valor de inventario@pre est´an tal cual en inventario, con excepci´on del valor que
tiene como clave nombre}
asegura: {Todos los pares clave-valor de inventario est´an en inventario@pre}
asegura: {En inventario el diccionario asociado a nombre, tendr´a la misma cantidad que antes y el precio ser´a
precio}
}'''

def actualizar_precio(inventario: dict[str, dict[str, int|float]], nombre: str, precio: float) -> None:
    if nombre in inventario.keys():
        inventario[nombre]["precio"] = precio


'''4. problema calcular valor inventario (in inventario: Diccionario ⟨ seq⟨Char⟩, Diccionario ⟨ seq⟨Char⟩, T ⟩⟩) : R {
requiere: {T ∈ [Z, R]}
requiere: {Ninguno de los Strings del inventario es vac´ıo}
asegura: {res es la suma, para cada producto, del precio multiplicado por la cantidad}
}'''

def calcular_valor_inventario(inventario: dict[str,dict[str, int|float]]) -> float:
    res: float = 0.0
    for producto in inventario.keys():
        valor: dict[str, int|float] = inventario[producto]  
        res += valor["precio"]*valor["cantidad"]
    return res