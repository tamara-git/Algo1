def devolver_el_doble_si_es_par(n:int) -> int:
    if n%2 == 0:
        return 2*n
    else:
        return n


print (devolver_el_doble_si_es_par (4))