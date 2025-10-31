'''Ejercicio 3. Veterinaria - Flujo de pacientes
Con el objetivo de organizar el flujo de pacientes, en una veterinaria se anotan los tipos de mascotas que van ingresando
al local. Se necesita identificar las consultas que involucran solo a perros y gatos. Por eso, se decide desarrollar una funci´on en
Python que encuentre la secuencia m´as larga de consultas consecutivas que solo contenga los tipos de mascota ”perro” o ”gato”.
Se pide implementar una funci´on que, dada una secuencia de strs, que representan los tipos de animales atendidos, devuelva el
´ındice donde comienza la subsecuencia m´as larga que cumpla con estas condiciones.
problema subsecuencia mas larga (in tipos pacientes atendidos : seq⟨str⟩) : Z {
requiere: {tipos pacientes atendidos tiene, por lo menos, un elemento ”perro” o ”gato”.}
asegura: {res es el ´ındice donde empieza la subsecuencia m´as larga de tipos pacientes atendidos que contenga solo
elementos ”perro” o ”gato”.}
asegura: {Si hay m´as de una subsecuencia de tama˜no m´aximo, res tiene el ´ındice de la primera.}
}'''

def subsecuencia_mas_larga(tipos_pacientes_atendidos: list[str]) -> int:
    maximo: int = 0
    cantidad: int = 1
    indice_max: int = 0
    indice_actual: int = 0
    for indice in range(len(tipos_pacientes_atendidos)-1):
        if (tipos_pacientes_atendidos[indice] == "perro" or tipos_pacientes_atendidos[indice] == "gato") and (tipos_pacientes_atendidos[indice+1] == "perro" or tipos_pacientes_atendidos[indice+1] == "gato"):
            cantidad += 1
        else:
            if cantidad > maximo:
                maximo = cantidad
                indice_max = indice_actual 
                indice_actual = indice + 1
                cantidad = 1
            else:
                cantidad = 1
                indice_actual = indice + 1
    if cantidad > maximo:
        maximo = cantidad
        indice_max = indice_actual 
    return indice_max

print(subsecuencia_mas_larga(["perro","gato","perro","tortuga","perro","perro","hamster", "perro","perro"]))
            
            


'''Ejercicio 14. Hospital - Alarma epidemiol´ogica
Necesitamos detectar la aparici´on de posibles epidemias. Para esto contamos con un lista de enfermedades infecciosas y los
registros de atenci´on por guardia dados por una lista expedientes. Cada expediente es una tupla con ID paciente y enfermedad
que motiv´o la atenci´on. Debemos devolver un diccionario cuya clave son las enfermedades infecciosas y su valor es la proporci´on
de pacientes que se atendieron por esa enfermedad. En este diccionario deben aparecer solo aquellas enfermedades infecciosas
cuya proporci´on supere cierto umbral.
problema alarma epidemiologica (in registros : seq⟨Z × str⟩, in infecciosas : seq⟨str⟩, in umbral : R) : dict<str, R> {
requiere: {0 < umbral < 1.}
asegura: {claves de res pertenecen a infecciosas.}
asegura: {Para cada enfermedad perteneciente a infecciosas, si el porcentaje de pacientes que se atendieron por esa
enfermedad sobre el total de registros es mayor o igual al umbral, entonces res[enfermedad] = porcentaje.}
asegura: {Para cada enfermedad perteneciente a infecciosas, si el porcentaje de pacientes que se atendieron por esa
enfermedad sobre el total de registros es menor que el umbral, entonces enfermedad no aparece en res.}
}'''

def porcentaje(cantidad: int, total: int) -> float:
    return cantidad/total

def alarma_epidemiologica(registros: list[tuple[int,str]], infecciosas: list[str], umbral: float) -> dict[str,float]:
    dict_aux: dict[str,float] = {}
    res: dict[str,float] = {}
    for registro in registros:
        enfermedad: str = registro[1]
        if enfermedad in infecciosas:
            if enfermedad not in dict_aux:
                dict_aux[enfermedad] = 1 
            else:
                dict_aux[enfermedad] += 1
    
    for infeccion in dict_aux.keys():
        if porcentaje(dict_aux[infeccion], len(registros)) >= umbral:
            res[infeccion] = porcentaje(dict_aux[infeccion], len(registros))
    return res
            



'''Ejercicio 15. Hospital - Empleado del mes
Dado un diccionario con la cantidad de horas trabajadas por empleado, en donde la clave es el ID del empleado y el valor es
una lista de las horas trabajadas por d´ıa, queremos saber quienes trabajaron m´as para darles un premio. Se deber´a buscar la o
las claves para la cual se tiene el m´aximo valor de cantidad total de horas, y devolverlas en una lista.
problema empleados del mes (horas:dicc<Z, seq⟨Z⟩) : seq⟨Z⟩ {
requiere: {No hay valores en horas que sean listas vac´ıas.}
asegura: {Si ID pertenece a res entonces ID pertence a las claves de horas.}
asegura: {Si ID pertenece a res, la suma de sus valores de horas es el m´aximo de la suma de elementos de horas de todos
los otros IDs.}
asegura: {Para todo ID de claves de horas, si la suma de sus valores es el m´aximo de la suma de elementos de horas de
los otros IDs, entonces ID pertenece a res.}
}'''

def horas_totales(horas: dict[int,list[int]]) -> list[tuple[int,int]]:
    res: list[tuple[int,int]] = []
    for empleado in horas.keys():
        horas_totales: int = 0
        lista_horas: list[int] = horas[empleado]
        for hora in lista_horas:
            horas_totales += hora
        res.append((empleado, horas_totales))
        
    return res 



def buscar_los_maximos(horasTotalesPorEmpleado:list[tuple[int,int]]) -> list[int]:
    maximo: int = horasTotalesPorEmpleado[0][1]
    maximo_ID: int = horasTotalesPorEmpleado[0][0]
    res: list[int] = []
    for elemento in horasTotalesPorEmpleado:
        hora_total: int = elemento[1]
        ID_actual: int = elemento[0]
        if hora_total > maximo:
            maximo = hora_total
            maximo_ID = ID_actual
    res.append(maximo_ID)
    
    for elemento in horasTotalesPorEmpleado:
        hora_total: int = elemento[1]
        ID_actual: int = elemento[0]
        if hora_total == maximo and ID_actual != maximo_ID:
            res.append(ID_actual)
    return res
    

def empleado_del_mes(horas:dict[int,list[int]]) -> list[int]:
    return buscar_los_maximos(horas_totales(horas))