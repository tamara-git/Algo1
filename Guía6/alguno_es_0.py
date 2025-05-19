#alguno_es_0(numero1, numero2): dados dos números racionales, decide si alguno de los dos es igual a 0

def alguno_es_cero(numero1:float,numero2:float) -> bool:
   return (numero1 == 0 or numero2 == 0 )

print (alguno_es_cero (0,3))