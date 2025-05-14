def min(a,b):
    if a<b:
        return a
    else:
        return b

def es_primo(n:int) -> bool:
    n = abs (n)
    if n == 0 or n == 1:
        return False
    
   #range(2,4) -> [2,3] 
    for i in range(2,n):
        if n % i == 0:
            return False
    return True


def cuantos_primos_en_rango(n:int,m:int) -> int:
    minimo = min(n,m) #definido en preludio
    maximo = max(n,m) #def en preludio
    res = 0
    for i in range(minimo,maximo+1):
        if es_primo(i):
            res = res + 1
    return res