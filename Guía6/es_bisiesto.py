# es_bisiesto(año): que indica si un año tiene 366 días. Recordar que un año es bisiesto si es múltiplo de 400,
#  o bien es múltiplo de 4 pero no de 100.

def es_bisiesto (año:int) -> bool:
     return (año % 400 == 0 or (año % 4 == 0 and not (año % 100 ==0)))

print (es_bisiesto (2025)) 