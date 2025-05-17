#lindo_nombre(nombre) que dado un nombre, si la longitud es igual o mayor a 5 devolver una frase que diga “Tu
#nombre tiene muchas letras!” y si no, “Tu nombre tiene menos de 5 caracteres”.

def lindo_nombre(nombre:str) -> str:
   if len(nombre) >= 5:
      return("Tu nombre tiene muchas letras!")
   else:
      return("Tu nombre tiene menos de 5 caracteres") 
   
print(lindo_nombre("Kiara"))
