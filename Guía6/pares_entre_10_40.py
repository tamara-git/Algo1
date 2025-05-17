#2. Escribir una función que imprima los números pares entre el 10 y el 40.

def pares_entre_10_40_while() -> None:
    i = 10
    while i <= 40:
        print(i)
        i += 2

pares_entre_10_40_while()

#hecho con for
def pares_entre_10_40 () -> None:
    for i in range(10,41,2):
        print(i)

pares_entre_10_40()