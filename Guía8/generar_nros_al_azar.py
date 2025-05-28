'''problema generar nros al azar (in cantidad: Z, in desde: Z, in hasta: Z) : Pila[Z] {
requiere: {cantidad ≥ 0}
requiere: {desde ≤ hasta}
asegura: {El tama˜no de res es igual a cantidad}
asegura: {Todos los elementos de res son valores entre desde y hasta (ambos inclusive), seleccionados aleatoriamente
con probabilidad uniforme}
Para generar n´umeros en un rango con probabilidad uniforme, pueden usar la funci´on 
random.randint(< desde >, < hasta >) que devuelve un n´umero en el rango indicado.
 Recuerden importar el módulo random con import random.
}
'''

'''p = Pila () # crea una pila
p.put (1) # apila un 1
elemento = p.get () # desapila
p.empty () # devuelve true si y solo si la pila está vacía'''

from queue import LifoQueue as Pila # importa LifoQueue y le asigna el alias Pila
import random 
def generar_nros_al_azar(cantidad:int, desde:int, hasta:int) -> Pila[int]:
    res: Pila[int] = Pila()

    for _ in range(cantidad):
        numero: int = random.randit(desde,hasta)
    res.put(numero)

    return res