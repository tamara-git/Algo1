'''Implementar una solución, que use pila, para el siguiente problema.
problema esta bien balanceada (in s: seq⟨Char⟩) : Bool {
requiere: {s solo puede tener números enteros, espacios y los símbolos '(', ')', '+', '-', '*', '/'}
asegura: {res = true ↔ (La cantidad de paréntesis de apertura '('es igual a la de cierre ')') y (Para todo prefijo de 's',
la cantidad de paréntesis de cierre no supera a la de apertura)}
}
Por cada paréntesis de cierre debe haber uno de apertura correspondiente antes de él. Las fórmulas pueden tener:
    - números enteros
    - operaciones básicas +, −, ∗ y /
    - paréntesis
    - espacios
Entonces las siguientes son fórmulas aritméticas con sus paréntesis bien balanceados:
1 + ( 2 x 3 = ( 2 0 / 5 ) )
10 * ( 1 + ( 2 * ( =1)))
Y la siguiente es una fórmula que no tiene los paréntesis bien balanceados:
1 + ) 2 x 3 ( ( )

}
'''

from queue import LifoQueue as Pila


# Hago una función que copie la pila original.
def copiar_pila(pila:Pila[str]) -> Pila[str]:
    pila_auxiliar: Pila[str] = Pila()
    pila_copia:  Pila[str] = Pila()

# invierto la pila en pila_auxiliar
    while not pila.empty():
        elemento: str = pila.get()
        pila_auxiliar.put(elemento)

# hago la copia y restauro la pila original.
    while not pila_auxiliar.empty():
        elemento: str = pila_auxiliar.get()
        pila_copia.put(elemento)
        pila.put(elemento)

    return pila_copia

def esta_bien_balanceada(pila:Pila[str]) -> bool:
    pila_copia: Pila[str] = copiar_pila(pila)
    cantidad_apertura: int = 0 
    cantidad_cierre: int = 0
    ultimo_elemento: str = pila_copia.get()
    operaciones_basicas: list[str] = ['+', '−', '∗', '/']

    # Miro el primer elemento, si es '(' o una operación básica es False, si es ')' o un numero, sigo recorriendo

    if ultimo_elemento in operaciones_basicas or ultimo_elemento == '(':
        return False
    
    else:

        while not pila_copia.empty():
            elemento: str = pila_copia.get()
            if elemento == ')':
                cantidad_cierre += 1
                
            elif elemento == str(int) or elemento in operaciones_basicas:
                continue
            elif elemento == '(' and cantidad_cierre: 
                cantidad_apertura += 1
            
        if cantidad_cierre == cantidad_apertura:
            return True
        else:
            return False