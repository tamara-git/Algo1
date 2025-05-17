#. Escribir una función de cuenta regresiva para lanzar un cohete. Dicha función irá imprimiendo desde el número que me
# pasan por parámetro (que será positivo) hasta el 1, y por último “Despegue”.

def cuenta_regresiva(x:int) -> None:
    for i in range(1,x+1):
        print(x+1-i) 
        i +=1
    print("Despegue")
cuenta_regresiva(10)

#con while
def cuenta_regresiva_while (x:int) -> None:
    i = x
    while i != 0:
        print(i)
        i-=1
    print("Despegue")

cuenta_regresiva_while(10)