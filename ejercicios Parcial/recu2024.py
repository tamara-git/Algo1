# 1) Billetera Virtual [2 puntos]


# En el presente ejercicio verificaremos el histórico de transacciones (el historial) de una billetera virtual.
# En esta billetera sólo se puede: recargar saldo (r), pagar un viaje (v), ver el balance actual (s), y salir (x).
# Cada transacción queda grabada con su correspondiente caracter en una lista que representa el historial.

# En historial tendremos una secuencia de caracteres donde:
# v: Realiza un viaje (todos los viajes son de $56)
# r: Recarga saldo (todas las recargas son de $350)
# s: Visualiza el saldo actual (no modifica el saldo)
# x: El usuario decide terminar el programa.

# Impementar la funcion verificar_transacciones() que dada una secuencia de caracteres s, devuelve el
# saldo de la billetera al momento de terminar el programa. La finalización del programa está determinada
# por: (1) aparición de una x, (2) el usuario está intentando hacer un pago sin saldo suficiente (en esta
# billetera virtual no se permite saldo negativo), (3) no hay más transacciones en la lista.

# problema verificar_transacciones(in s: String) : Z{
# requiere: {|s|>0}
# requiere: {s sólo puede contener los caracteres "r", "x", "v" o "s"}
# asegura {res >= 0}
# asegura: {res = ($350 * #ap_antes_corte("r", s)) - ($56 * #ap_antes_corte("v", s))}
# }
# problema #ap_antes_corte(in c: char, in s: String) : z{
# requiere: {True}
# asegura: {res = cantidad de veces que aparece c desde el inicio hasta que: aparece una x, o que el 
# cálculo del saldo se hace negativo}
# }
# Ejemeplo 1: dado el siguiente historial
# s = "ssrvvrrvvsvvsxrvvv"
# se debería devolver res = 714

# Ejemplo 2: dado el siguiente historial
# s = "ssrvvvvsvvsvvv"
# se deberia devolver res = 14 (en este caso el programa termina porque el saldo no alcanza para realizar un viaje que está entre las transacciones)


def verificar_transacciones(s: str) -> int:
    res = (350 * ap_antes_corte("r",s)) - (56 * ap_antes_corte("v",s))
    return res


def ap_antes_corte(c: str, s: str) -> int:
    saldo: int = 0
    res: int = 0
    for i in range(len(s)):
        while s[i] != "x" and saldo > 0:    
            if s[i] == c:
                cantidad += 1
                saldo += letra_por_numero(c)
            else:
                saldo += letra_por_numero(s[i])
            
    return res
            
def letra_por_numero(c:str) -> int:
    res: int = 0
    if c == "r":
        res = 350
    if c == "v":
        res = -56
    return res                  



