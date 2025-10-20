'''Ejercicio 1. Implementar una soluci´on para el siguiente problema.
problema generar nros al azar (in cantidad: Z, in desde: Z, in hasta: Z) : Pila[Z] {
requiere: {cantidad ≥ 0}
requiere: {desde ≤ hasta}
asegura: {El tama˜no de res es igual a cantidad}
asegura: {Todos los elementos de res son valores entre desde y hasta (ambos inclusive), seleccionados aleatoriamente
con probabilidad uniforme}
}'''
import random
from queue import LifoQueue as Pila
'''p = Pila () # crea una pila
p . put (1) # apila un 1
elemento = p . get () # desapila
p . empty () # devuelve true si y solo si la pila está vacía'''


def generar_nros_al_azar(cantidad:int, desde:int, hasta:int) -> Pila[int]:
    res: Pila[int] = Pila()

    for _ in range(cantidad):
        numero: int = random.randit(desde,hasta)
    res.put(numero)

    return res

'''Ejercicio 2. Implementar una soluci´on para el siguiente problema.
problema cantidad elementos (in p: Pila) : Z {
requiere: {True}
asegura: {res es igual a la cantidad de elementos que contiene p}
}
No se puede utilizar la funci´on LifoQueue.qsize(). Tener en cuenta que, al usar get() para recorrer la pila, se modifica el
par´ametro de entrada, ya que los elementos se eliminan al accederse. Dado que la especificaci´on lo define como de tipo in, 
debe restaurarse posteriormente.'''



def copiar_pila(p: Pila[int]) -> Pila[int]:
    pila_aux: Pila[int] = Pila()
    pila_copia: Pila[int] = Pila()
    while not p.empty():
        elemento: int = p.get()
        pila_aux.put(elemento)
    
    while not pila_aux.empty():
        elemento: int = pila_aux.get()
        pila_copia.put(elemento)
        p.put(elemento)
    return pila_copia
    

def cantidad_elementos(p: Pila) -> int:
    pila_copia: Pila[int] = copiar_pila(p)
    cantidad: int = 0
    while not pila_copia.empty():
        pila_copia.get()
        cantidad += 1
    return cantidad

'''Ejercicio 3. Implementar una soluci´on para el siguiente problema.
problema buscar el maximo (in p: Pila[Z]) : Z {
requiere: {p no est´a vac´ıa}
asegura: {res es un elemento de p}
asegura: {res es mayor o igual a todos los elementos de p}
}'''

def buscar_el_maximo(p: Pila[int]) -> int:
    pila_copia: Pila[int] = copiar_pila(p)
    maximo: int = pila_copia.get()
    while not pila_copia.empty():
        elemento_actual: int = pila_copia.get()
        if elemento_actual > maximo:
            maximo = elemento_actual
    return maximo

'''Ejercicio 4. Implementar una soluci´on para el siguiente problema.
problema buscar nota maxima (in p: Pila[seq⟨Char⟩×Z]) : seq⟨Char⟩ ×Z {
requiere: {p no est´a vac´ıa}
requiere: {los elementos de p no tienen valores repetidos en la segunda posici´on de las tuplas}
asegura: {res es una tupla de p}
asegura: {No hay ning´un elemento en p cuya segunda componente sea mayor que la segunda componente de res }
}'''



def buscar_nota_maxima(p: Pila[tuple[str,int]]) -> tuple[str,int]: 
    pila_copia: Pila[tuple[str,int]] = copiar_pila(p)
    maximo: tuple[str,int] = pila_copia.get()
    while not pila_copia.empty():
        elemento_actual: tuple[str,int] = pila_copia.get()
        if elemento_actual[1] > maximo[1]:
            maximo = elemento_actual
    return maximo  


'''Ejercicio 5. Implementar una soluci´on, que use pila, para el siguiente problema.
problema esta bien balanceada (in s: seq⟨Char⟩) : Bool {
requiere: {s solo puede tener n´umeros enteros, espacios y los s´ımbolos ’(’, ’)’, ’+’, ’-’, ’*’, ’/’}
asegura: {res = true ↔ (La cantidad de par´entesis de apertura ’(´es igual a la de cierre ’)’) y (Para todo prefijo de ‘s‘, la
cantidad de par´entesis de cierre no supera a la de apertura)}
}
Por cada par´entesis de cierre debe haber uno de apertura correspondiente antes de ´el. Las f´ormulas pueden tener:
n´umeros enteros
operaciones b´asicas +, −, ∗ y /
par´entesis
espacios
Entonces las siguientes son f´ormulas aritm´eticas con sus par´entesis bien balanceados:
1 + ( 2 x 3 = ( 20 / 5 ) )
10 * ( 1 + ( 2 * ( =1)))
Y la siguiente es una 0f´ormula que no tiene los par´entesis bien balanceados:
1 + ) 2 x 3 ( ( '''

def esta_bien_balanceada(s:str) -> bool:
    res: bool = False
    cant_inicio: int = 0
    cant_final: int = 0
    pila: Pila[str] = Pila()
    for i in range(len(s)):
        if s[i] == "(" :
            pila.put(s[i])
            cant_inicio += 1
        if s[i] == ")":
            pila.put(s[i])
            cant_final += 1
    if cant_inicio == cant_final and pila.get() == ")":
        res = True 
    return res


'''Ejercicio 7. Implementar una soluci´on para el siguiente problema.
problema intercalar (in p1: Pila, in p2: Pila) : Pila {
requiere: {p1 y p2 tienen la misma cantidad de elementos}
asegura: {res solo contiene los elementos de p1 y p2}
asegura: {res contiene todos los elementos de p1 y p2, intercalados y respetando el orden original}
asegura: {El tope de la pila res es el tope de p2}
asegura: {El tama˜no de res es igual al doble del tama˜no de p1}
}
'''    
def invertir_pila(pila: Pila) -> Pila:
    lista_testeo: list = []
    res: Pila = Pila ()
    while not pila.empty():
        elemento = pila.get()
        res.put(elemento)
        lista_testeo.append(elemento)
    return res

def intercalar(p1: Pila, p2: Pila) -> Pila:
    res: Pila = Pila()
    p1_copia: Pila = copiar_pila(p1)
    p2_copia: Pila = copiar_pila(p2)
    while not p2_copia.empty():
        elemento_p1 = p1_copia.get()
        elemento_p2 = p2_copia.get()
        res.put(elemento_p2)
        res.put(elemento_p1) 

    return invertir_pila(res)



def invertir_pila_testeo(pila: Pila) -> list:
    lista_testeo: list = []
    res: Pila = Pila ()
    while not pila.empty():
        elemento = pila.get()
        res.put(elemento)
        lista_testeo.append(elemento)
    return lista_testeo

def intercalar_testeo(p1: Pila, p2: Pila) -> Pila:
    res: Pila = Pila()
    p1_copia: Pila = copiar_pila(p1)
    p2_copia: Pila = copiar_pila(p2)
    while not p2_copia.empty():
        elemento_p1 = p1_copia.get()
        elemento_p2 = p2_copia.get()
        res.put(elemento_p2)
        res.put(elemento_p1) 

    return invertir_pila_testeo(res)


