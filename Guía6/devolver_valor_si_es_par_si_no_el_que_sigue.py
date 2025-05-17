#devolver_valor_si_es_par_si_no_el_que_sigue(numero): devuelve el mismo número si es par, y si no, el siguiente.
# Analizar distintas formas de implementación (usando un if-then-else y dos if). ¿Todas funcionan?

def devolver_valor_si_es_par_si_no_el_que_sigue(numero:int) -> int:
    if numero%2 == 0:
        return numero
    else:
        return (numero + 1)
    

print(devolver_valor_si_es_par_si_no_el_que_sigue(2))
