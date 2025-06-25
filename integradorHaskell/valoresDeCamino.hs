{-Implementar la funci´on valoresDeCamino :: Tablero -> Camino ->[Int]
problema valoresDeCamino (t: Tablero, c: Camino) : seq⟨Z⟩ {
requiere: {El tablero t es un tablero bien formado, es decir, la longitud de todas las filas es la misma, y tienen al
menos un elemento}
requiere: {Existe al menos una columna en el tablero t }
requiere: {El tablero t no es vac´ıo, todos los n´umeros del tablero son positivos, mayores estrictos a 0}
requiere: {El camino c es un camino v´alido, es decir, secuencia de posiciones adyacentes en la que solo es posible
desplazarse hacia la posici´on de la derecha o hacia abajo y todas las posiciones est´an dentro de los limites del tablero
t}
asegura: {res es igual a la secuencia de n´umeros que est´an en el camino c, ordenados de la misma forma que aparecen
las posiciones correspondientes en el camino.}
}-}
{-Fila = seq⟨Z⟩
Tablero = seq⟨F ila⟩
Posicion = Z × Z – Observaci´on: las posiciones son: (fila, columna)
Camino = seq⟨Posicion⟩-}

type Fila = [Int]
type Tablero = [[Int]]
type Camino = [(Int,Int)]

aplanar :: Tablero -> [Int]
aplanar [x] = x
aplanar (x:xs) = x ++ aplanar xs 

sumarTuplas :: (Int,Int) -> (Int,Int) -> (Int,Int)
sumarTuplas (a,b) (c,d) = (a+c, b+d)



--Cantidad de filas que tiene el tablero. Devuelve algo del tipo (filas,0)
filas :: Tablero -> (Int,Int)
filas [x] = (1,0)
filas (x:xs) = sumarTuplas (1,0) (filas xs)

--Cantidad de columnas que tiene el tabler. Devuelve algo del tipo (0,columnas)
columnas :: [Int] -> (Int,Int)
columnas [x] = (0,1)
columnas (x:xs) = sumarTuplas (0,1) (columnas xs)


--Ultima posicion del tablero. Devuelve algo del tipo (filas,columnas)
limiteMatriz :: Tablero -> (Int,Int)
limiteMatriz (x:xs) = sumarTuplas (filas (x:xs)) (columnas x)


todosElementosIguales :: [Int] -> [Int] -> Bool
todosElementosIguales [x] [y] | x == y = True
                              | otherwise = False 
todosElementosIguales (x:xs) (y:ys) | x == y = todosElementosIguales xs ys
                                    | otherwise = False


pertenece :: Int -> [Int] -> Bool 
pertenece e [x] | e == x = True
                | otherwise = False
pertenece e (x:xs) | e == x = True
                   | otherwise = pertenece e xs
                   

perteneceYDevuelvePosicion :: Int -> [Int] -> Int 
perteneceYDevuelvePosicion e [x] | e == x = 1
                                 | otherwise = 0
perteneceYDevuelvePosicion e (x:xs) | e == x = 1
                                    | otherwise = 1 + perteneceYDevuelvePosicion e xs


devuelveFila :: Tablero -> Int -> Int
devuelveFila [x] e = 1
devuelveFila (x:xs) e | pertenece e x == True = 1
                      | otherwise =  1 + (devuelveFila (xs) e)


armarListaColumna :: Tablero -> [Int]
armarListaColumna [x] = [head x]
armarListaColumna (x:xs) = [head x] ++ armarListaColumna xs

quitarColumna :: Tablero -> [[Int]]
quitarColumna [x] = [tail(aplanar [x])]
quitarColumna (x:xs) = [tail (aplanar [x])] ++ quitarColumna xs


devuelveColumna :: Tablero -> Int -> Int
devuelveColumna [x] e = perteneceYDevuelvePosicion e (armarListaColumna [x])
devuelveColumna (x:xs) e | pertenece e (armarListaColumna (x:xs)) = 1
                         | otherwise = 1 + devuelveColumna (quitarColumna (x:xs)) e


posicion ::  Tablero -> Int -> (Int,Int)
posicion [x] e = (devuelveFila [x] e, devuelveColumna [x] e)
posicion (x:xs) e = (devuelveFila (x:xs) e, devuelveColumna (x:xs) e)


valoresDeCamino :: Tablero -> Camino -> [Int]
valoresDeCamino [x] [(a,b)] | posicion [x] head(aplanar[x]) == (a,b) = [head x]
                            | otherwise = valoresDeCamino [(tail(aplanar[x]))] [(a,b)]
