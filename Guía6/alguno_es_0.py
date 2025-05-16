#alguno_es_0(numero1, numero2): dados dos números racionales, decide si alguno de los dos es igual a 0

def alguno_es_cero(x:float,y:float) -> bool:
   return (x == 0 or y == 0 )

print (alguno_es_cero (0,3))