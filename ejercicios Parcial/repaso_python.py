from queue import Queue as Cola
# def desordenar_filas(matriz: list[list[int]]):
#     matriz_nueva: list[list[int]] = []
#     for i in range(len(matriz)-1,-1,-1):
#         elemento: list[int] = matriz[i]
#         matriz_nueva.append(elemento)


# def cambiar_matriz(matriz: list[list[int]]):
#     return desordenar_filas(matriz)



def cambiar_matriz(a:list[list[int]]) -> None:
    maximo: int = len(a[0])*len(a)
    for f in range(len(a)):
        for c in range(len(a[0])):
            if a[f][c] == maximo:
                maximo = 1
            else:
                a[f][c] += 1


def promedio_de_salidas(registro: dict[str,list[int]]) -> dict[str, tuple[int,float]]:
    res: dict[str,tuple[int,float]] = {}
    for integrante in registro.keys():
        ganadas: int = 0
        tiempos: float = 0.0
        for sala in registro[integrante]:
            if sala > 0 and sala < 61:
                ganadas += 1
                tiempos += sala 
        if ganadas == 0:
            res[integrante] = (0,0.0)
        else:
            res[integrante] = (ganadas, tiempos/ganadas)
    return res


def reordenar_cola_priorizando_vips(filaClientes: Cola[tuple[str,str]]) -> Cola[str]:
    res_vip: Cola[str] = Cola()
    res_comun: Cola[str] = Cola()
    cola_ordenada: Cola[str] = Cola()
    filaClientesRestaurar: Cola[tuple[str,str]] = Cola()
    while not filaClientes.empty():
        tupla: tuple[str,str] = filaClientes.get()
        filaClientesRestaurar.put(tupla)
        cliente: str = tupla[0]
        tipo_afiliado: str = tupla[1] 
        if tipo_afiliado == "vip":
            res_vip.put(cliente)
        else:
            res_comun.put(cliente)
    
    while not res_vip.empty():
        cliente_vip: str = res_vip.get()
        cola_ordenada.put(cliente_vip)

    while not res_comun.empty():
        cliente_comun: str = res_comun.get()
        cola_ordenada.put(cliente_comun)
    
    while not filaClientesRestaurar.empty():
        tupla: tuple[str,str] = filaClientesRestaurar.get()
        filaClientes.put(tupla)
    
    return cola_ordenada


def reordenar_cola_priorizando_vips_mostrar(filaClientes: Cola[tuple[str,str]]) -> list[str]:
    res_vip: Cola[str] = Cola()
    res_comun: Cola[str] = Cola()
    cola_ordenada: Cola[str] = Cola()
    filaClientesRestaurar: Cola[tuple[str,str]] = Cola()
    lista: list[str] = []
    while not filaClientes.empty():
        tupla: tuple[str,str] = filaClientes.get()
        filaClientesRestaurar.put(tupla)
        cliente: str = tupla[0]
        tipo_afiliado: str = tupla[1] 
        if tipo_afiliado == "vip":
            res_vip.put(cliente)
        else:
            res_comun.put(cliente)
    
    while not res_vip.empty():
        cliente_vip: str = res_vip.get()
        cola_ordenada.put(cliente_vip)
        lista.append(cliente_vip)

    while not res_comun.empty():
        cliente_comun: str = res_comun.get()
        cola_ordenada.put(cliente_comun)
        lista.append(cliente_comun)

    while not filaClientesRestaurar.empty():
        tupla: tuple[str,str] = filaClientesRestaurar.get()
        filaClientes.put(tupla)
    #print(res.queue)
    return lista



def nivel_de_ocupacion(camas_por_piso: list[list[bool]]) -> list[float]:
    res: list[float] = [] 
    filas: int = len(camas_por_piso)
    columnas: int = len(camas_por_piso[0])
    cantidad_camas: int = columnas
    for fila in range(filas):
        cantidad: int = 0
        for columna in range(columnas):
            if camas_por_piso[fila][columna] == True:
                cantidad += 1
        res.append(cantidad/cantidad_camas)
    return res


    
