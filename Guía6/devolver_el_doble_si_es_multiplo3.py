#devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(numero): en otro caso, devolver el número original.
# Analizar distintas formas de implementación (usando un if-then-else, dos if, o alguna opción de operación lógica).
#  ¿Todas funcionan? ¿Cuál es el resultado si la entrada es 18?

#problema devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(numero:Z) : Z {
#   requiere: {True}
#   asegura: { res = 2*n ↔ n mod 3 = 0 }
#   asegura: { res = 3*n ↔ n mod 9 = 0 } 
#   asegura: { en otros casos, res = n }
#               }
#}
def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(numero:int) -> int:
    if numero % 3 == 0:
        return 2*numero 
    elif numero % 9 == 0:
        return 3*numero
    else:
        return numero
    
print (devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(9))
