from math import sqrt, ceil

'''1. problema imprimir_saludo (in nombre: String) {
requiere: { True }
asegura: {imprime “Hola < nombre >"por pantalla}
}
'''

def imprimir_saludo(nombre: str) -> None: 
    return("Hola " + nombre)

print(imprimir_saludo("Pablo"))

'''2. raiz_cuadrada_de(numero): que devuelva la raíz cuadrada del número'''

def raiz_cuadrada_de_(numero: float) -> None:
    return (sqrt(numero))
print(raiz_cuadrada_de_(4))

'''3. fahrenheit_a_celsius(temp_far): que convierta una temperatura en grados Fahrenheit a grados Celcius.
problema fahrenheit_a_celsius (in t: R) : R {
requiere: { T rue }
asegura: {res = ((t − 32) × 5)/9}
}'''

def fahrenheit_a_celsius(t: float) -> float:
    return(((t-32)* 5)/9)

print(fahrenheit_a_celsius(32))

'''4. imprimir_dos_veces(estribillo): que imprima dos veces el estribillo de una canción. 
Nota: Analizar el comportamiento del operador (*) con strings.
'''

def imprimir_dos_veces(estribillo: str) -> None:
    return(2*estribillo)

print(imprimir_dos_veces("De aquel amor\nDe música ligera\nNada nos libra\nNada más queda"))


'''5. problema es_multiplo_de (in n: Z, in m:Z) : Bool {
requiere: {m ̸= 0}
asegura: {(res = true) ↔ (existe un k ∈ Z tal que n = m × k)}
}'''

def es_multiplo_de (n: int, m: int) -> bool:
    return n % m == 0   
print(es_multiplo_de(5,2))

'''6. es_par(numero): que indique si numero es par (usar la función es_multiplo_de()).'''

def es_par(numero: int) -> bool:
    return(es_multiplo_de(numero,2))

print(es_par(4))

'''7. cantidad_de_pizzas(comensales, min_cant_de_porciones) que devuelva la cantidad de pizzas que necesitamos
para que cada comensal coma como mínimo min_cant_de_porciones porciones de pizza. Considere que cada pizza
tiene 8 porciones y que se prefiere que sobren porciones.'''

def cantidad_de_pizzas(comensales: int, min_cant_de_porciones: int) -> int:
    return(ceil((comensales * min_cant_de_porciones) / 8))

print(cantidad_de_pizzas(17,2))
