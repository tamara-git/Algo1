'''Ejercicio 3. Veterinaria - Flujo de pacientes
Con el objetivo de organizar el flujo de pacientes, en una veterinaria se anotan los tipos de mascotas que van ingresando
al local. Se necesita identificar las consultas que involucran solo a perros y gatos. Por eso, se decide desarrollar una función en
Python que encuentre la secuencia más larga de consultas consecutivas que solo contenga los tipos de mascota ”perro” o ”gato”.
Se pide implementar una función que, dada una secuencia de strs, que representan los tipos de animales atendidos, devuelva el
índice donde comienza la subsecuencia más larga que cumpla con estas condiciones.
problema subsecuencia mas larga (in tipos pacientes atendidos : seq⟨str⟩) : Z {
requiere: {tipos pacientes atendidos tiene, por lo menos, un elemento ”perro” o ”gato”.}
asegura: {res es el índice donde empieza la subsecuencia más larga de tipos pacientes atendidos que contenga solo
elementos ”perro” o ”gato”.}
asegura: {Si hay más de una subsecuencia de tamaño máximo, res tiene el índice de la primera.}
}'''

def subsecuencia_mas_larga(tipos_pacientes_atendidos: list[str]) -> int:
    contador: int = 1
    contador_maximo: int = 0
    lista_1er_indice: list[int] = []

    for indice in range(len(tipos_pacientes_atendidos)-1):
        if tipos_pacientes_atendidos[indice] in ["perro","gato"] and tipos_pacientes_atendidos[indice + 1] in ["perro","gato"]:
            lista_1er_indice.append(indice)
            contador += 1
            if contador != 2:
                lista_1er_indice.pop()

        else:
            if contador > contador_maximo:
                contador_maximo = contador
                contador = 1
                
        if contador == contador_maximo:
                lista_1er_indice.pop()

      
    return lista_1er_indice.pop()
   
print(subsecuencia_mas_larga(["gato","gato","perro","gato","tortuga","carpincho", "mono", "perro","gato","perro","gato"]))


