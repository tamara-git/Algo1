def es_multiplo_de(n: int,m: int) -> bool:
    return n % m == 0

def es_par (n:int) -> bool:
    return es_multiplo_de(n,2)

print (es_par (3))
