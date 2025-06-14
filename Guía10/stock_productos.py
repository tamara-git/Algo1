''''Veterinaria - Stock
En la veterinaria ”Exactas’s pets”, al finalizar cada día, el personal registra en papeles los nombres y la cantidad actual de
los productos cuyo stock ha cambiado. Para mejorar la gesti´on, desde la direcci´on de la veterinaria han pedido desarrollar una
soluci´on en Python que les permita analizar las fluctuaciones del stock. Se pide implementar una funci´on, que reciba una lista
de tuplas donde cada tupla contiene el nombre de un producto y su stock en ese momento. La funci´on debe procesar esta lista
y devolver un diccionario que tenga como clave el nombre del producto y como valor una tupla con su m´ınimo y m´aximo stock
hist´orico registrado.
problema stock productos (in stock cambios : seq⟨str × Z⟩) : seq⟨Z⟩ {
requiere: {Todos los elementos de stock cambios est´an formados por un str no vac´ıo y un entero ≥ 0.}
asegura: {res tiene como claves solo los primeros elementos de las tuplas de stock cambios (o sea, un producto).}
asegura: {res tiene como claves todos los primeros elementos de las tuplas de stock cambios.}
asegura: {El valor en res de un producto es una tupla de cantidades. Su primer elemento es la menor cantidad de ese
producto en stock cambios y como segundo valor el mayor.}
}'''

def minimo_stock(stock_cambios: list[tuple[str,int]], producto: str) -> int:
    lista_producto_stocks: list[tuple[str,int]] = []

    for indice in range(len(stock_cambios)):
        if stock_cambios[indice][0] == producto:
            lista_producto_stocks.append(stock_cambios[indice])
        else:
            continue


    minimo: int = lista_producto_stocks[0][1]
    
    for indice in range(len(lista_producto_stocks)):
            if minimo > lista_producto_stocks[indice][1]:
                minimo = lista_producto_stocks[indice][1]

    return  minimo


def maximo_stock(stock_cambios: list[tuple[str,int]], producto: str) -> int:
    lista_producto_stocks: list[tuple[str,int]] = []

    for indice in range(len(stock_cambios)):
        if stock_cambios[indice][0] == producto:
            lista_producto_stocks.append(stock_cambios[indice])
        else:
            continue


    maximo: int = lista_producto_stocks[0][1]
    
    for indice in range(len(lista_producto_stocks)):
            if maximo < lista_producto_stocks[indice][1]:
                maximo = lista_producto_stocks[indice][1]

    return maximo


def stock_productos(stock_cambios: list[tuple[str,int]]) -> dict[str,tuple[str,str]]:
    res: dict[str,tuple[str,str]] = {}
    for (producto,cantidad) in stock_cambios:
        if producto not in res.keys():
            res[producto] = ((minimo_stock(stock_cambios, producto), maximo_stock(stock_cambios, producto)))
    
    return res


print(stock_productos([("remera",1),("remera",4),("top",7),("cargo",8),("top",4),("cargo",2)]))