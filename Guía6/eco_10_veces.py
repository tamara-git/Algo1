#Escribir una función que imprima la palabra “eco” 10 veces.

def eco_10_veces_while() -> str:
    i = 1
    res = "eco"
    while i <= 10:
        print (res)
        i += 1
eco_10_veces_while()

def eco_10_veces() -> str:
    for i in range(10):
        print("eco")
eco_10_veces()

