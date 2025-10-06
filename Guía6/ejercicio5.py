'''1. devolver_el_doble_si_es_par(numero); que devuelve el doble del número en caso de ser par y el mismo número en
caso contrario.

devolver_el_doble_si_es_par(numero: Z) -> Z {
{requiere: True }
{asegura: si n es par res = 2*numero, en otro caso res = numero}
'''
def devolver_el_doble_si_es_par(numero:int) -> int:
    if numero % 2 == 0: 
        return 2*numero 
    else:
        return numero
    
'''2.devolver_valor_si_es_par_sino_el_que_sigue(numero); que devuelve el mismo número si es par y sino el siguiente.
Analizar distintas formas de implementación (usando un if-then-else, y 2 if), todas funcionan?'''

def devolver_valor_si_es_par_sino_el_que_sigue(numero: int) -> int:
    if numero % 2 == 0:
        return numero
    else:
        return numero + 1


'''3.devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(numero). En otro caso devolver el número ori-
ginal. Analizar distintas formas de implementación (usando un if-then-else, y 2 if, usando alguna opción de operación
lógica), todas funcionan? Cuál es el resultado si la entrada es 18?

devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(numero: Z) -> Z {
{requiere: True }
{asegura: si n es multiplode3, res = 2*numero, si n es multiplode9 res = 3*numero, en otro caso res = numero}

'''


def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(numero:int) -> int: 
    if numero % 9 == 0:
        return numero*3
    if numero % 3 == 0:
        return numero*2
    else:
        return numero

print(devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(18))

'''4.lindo_nombre(nombre) que dado un nombre, si la longitud es igual o mayor a 5 devolver una frase que diga Tu
nombre tiene muchas letras! y sino, Tu nombre tiene menos de 5 caracteres.'''

def lindo_nombre(nombre: str) -> str:
    if len(nombre) >= 5:
        return ("¡Tu nombre tiene muchas letras!")
    else: 
        return("Tu nombre tiene menos de 5 caracteres.")
    

print(lindo_nombre("brun"))

'''5. elRango(numero) que imprime por pantalla "Menor a 5" si el número es menor a 5, "Entre 10 y 20" si el número está
en ese rango y "Mayor a 20" si el número es mayor a 20.'''

def elRango(numero: int) -> str:
    if numero < 5:
        return "Menor a 5"
    if 10 <= numero <=20:
        return "Entre 10 y 20"
    if numero > 20:
        return "Mayor a 20"
    else:
        return "Entre 5 y 10 estricto"
    

'''En Argentina una persona del sexo femenino se jubila a los 60 años, mientras que aquellas del sexo masculino se jubilan
a los 65 años. Quienes son menores de 18 años se deben ir de vacaciones junto al grupo que se jubila. Al resto de
las personas se les ordena ir a trabajar. Implemente una función que, dados los parámetros de sexo (F o M) y edad,
imprima la frase que corresponda según el caso: "Andá de vacaciones" o "Te toca trabajar".'''

def jubilacion(sexo: str, edad: int) -> str:
    if sexo == "F" and edad >= 60:
        return "Andá de vacaciones"
    if sexo == "M" and edad >= 65:
        return "Andá de vacaciones"
    if edad < 18:
        return "Andá de vacaciones"
    else:
        "Te toca trabajar"