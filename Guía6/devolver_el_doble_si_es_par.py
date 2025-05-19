#problema devolver_el_doble_si_es_par (in n:Z):Z {
# requiere = {True}
# asegura = {si el resto de dividir a n por dos es 0, entonces res = 2*n, en otro caso res = n}
# }

def devolver_el_doble_si_es_par(n:int) -> int:
    if n%2 == 0:
        return 2*n
    else:
        return n


print (devolver_el_doble_si_es_par (4))