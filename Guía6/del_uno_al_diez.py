#Escribir una función que imprima los números del 1 al 10.

def del_uno_al_diez() -> None:
    i = 1
    while i <= 10:
        print (i)
        i+=1 

del_uno_al_diez()

#con for
def del_uno_al_diez_2() -> None:
    for i in range(1,11):
        print(i)

del_uno_al_diez_2() 