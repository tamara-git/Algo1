#problema imprimir_saludo (in nombre: String) {
#requiere: { True }
#asegura: {imprime “Hola < nombre >"por pantalla}
#}

def imprimir_saludo (nombre: str) -> None:
    return ("Hola" + nombre)

print(imprimir_saludo(" Pablo"))