#elRango(numero) que imprime por pantalla “Menor a 5” si el número es menor a 5, “Entre 10 y 20” si el número está
#en ese rango y “Mayor a 20” si el número es mayor a 20.

def elRango(numero:int) -> str:
    if numero < 5:
        return("Menor a 5")
    elif numero >= 10 and numero <= 20:
        return ("Entre 10 y 20")
    elif numero > 20:
        return("Mayor a 20")

print(elRango(40))
print(elRango(4))
print(elRango(11))