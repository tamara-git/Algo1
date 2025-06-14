'''Veterinaria - Filtrar c´odigos de barra
El hijo del due˜no de la veterinaria, cuya actividad principal es ver tik toks, cree que los productos cuyos c´odigos de barras
terminan en n´umeros primos son especialmente auspiciosos y deben ser destacados en la tienda. Luego de convencer a su padre
de esta idea, solicita una funci´on en Python que facilite esta gesti´on. Se pide implementar una funci´on que, dada una secuencia de
enteros, cada uno representando un c´odigo de barras de un producto, cree y devuelva una nueva lista que contenga ´unicamente
aquellos n´umeros de la lista original cuyos ´ultimos tres d´ıgitos formen un n´umero primo (por ejemplo, 101, 002 y 011).
Nota: Un n´umero primo es aquel que solo es divisible por s´ı mismo y por 1. Algunos ejemplos de n´umeros primos de hasta
tres d´ıgitos son: 2, 3, 5, 101, 103, 107, etc.
problema filtrar codigos primos (in codigos barra : seq⟨Z⟩ ) : seq⟨Z⟩ {
requiere: {Todos los enteros de codigos barra tienen, por lo menos, 3 d´ıgitos.}
requiere: {No hay elementos repetidos en codigos barra.}
asegura: {Los ´ultimos 3 d´ıgitos de cada uno de los elementos de res forman un n´umero primo.}
asegura: {Todos los elementos de codigos barra cuyos ´ultimos 3 d´ıgitos forman un n´umero primo est´an en res.}
asegura: {Todos los elementos de res est´an en codigos barra.}
}
'''
def es_primo(numero: int) -> bool:
    variable: int = 1
    divisor: int = 0
    while variable <= numero:
        if numero % variable == 0:
            divisor += 1
            variable += 1
        else:
            variable += 1
     
    if divisor == 2:
        return True
    return False


def filtrar_codigos_primos(codigos_barra:(list[int])) -> list[int]:
    lista_primos

    for numero in codigos_barra:
        if es_primo(numero):
