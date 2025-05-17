# voy a crear la función altura_pino que convierta la altura de metros a centímetros
def altura_pino (metros:int) -> int:
    return (100*metros)

def peso_pino (metros:int) -> int:
    if altura_pino(metros) <=300: 
        return (altura_pino(metros)*3)
    else:
        return (900 + (altura_pino(metros)-300)*2) 

print(peso_pino(5))

# Definir la función es_peso_util, recibe un peso en kg y responde si un pino de ese peso le sirve a la fábrica
def es_peso_util(peso:int) -> bool:
    return(peso >= 400 and peso <=1000)

print(es_peso_util(1000))

#Definir la función sirve_pino, recibe la altura de un pino y responde si un pino de ese peso le sirve a la fábrica.
def sirve_pino(altura:int) -> bool:
    return(es_peso_util(peso_pino(altura)))

print (sirve_pino(5))
