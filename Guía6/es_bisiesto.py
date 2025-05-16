# es_bisiesto(año): que indica si un año tiene 366 días. Recordar que un año es bisiesto si es múltiplo de 400,
#  o bien es múltiplo de 4 pero no de 100.

def es_bisiesto (x:int) -> bool:
     return (x % 400 == 0 or (x % 4 == 0 and not (x % 100 ==0)))

print (es_bisiesto (2025)) 