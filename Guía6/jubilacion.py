#En Argentina una persona del sexo femenino se jubila a los 60 años, mientras que aquellas del sexo masculino se jubilan
# a los 65 años. Quienes son menores de 18 años se deben ir de vacaciones junto al grupo que se jubila. Al resto de
# las personas se les ordena ir a trabajar. Implemente una función que, dados los parámetros de sexo (F o M) y edad,
# imprima la frase que corresponda según el caso: “Andá de vacaciones” o “Te toca trabajar”.

def jubilacion(sexo:str,edad:int) -> str:
    if sexo == "F" and  18<=edad<60:
        return("Te toca trabajar") 
    elif sexo == "M" and 18<=edad<65:
        return("Te toca trabajar") 
    else:
        return("Andá de vacaciones") 
    
print(jubilacion("F",70))
print(jubilacion("M",10))
print(jubilacion("F",18))