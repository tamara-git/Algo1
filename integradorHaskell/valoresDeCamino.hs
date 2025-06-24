{-Implementar la funci´on valoresDeCamino :: Tablero ->Camino ->[Int]
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

{-
posicionDevuelveNumero :: Tablero -> (Int, Int) -> (Int,Int) -> Int
posicionDevuelveNumero [x] (1,1) = head (aplanar [x])
posicionDevuelveNumero (x:xs) (a,b) | (a,b) ==  = head (aplanar [x])
                                    | otherwise = 
-}
--Me devuelve qué fila del tablero es


todosElementosIguales :: [Int] -> [Int] -> Bool
todosElementosIguales (x:xs) (y:ys) | x != y = False
                                    | otherwise = todosElementosIguales xs (y:ys)

perteneceListaATablero :: [Int] -> Tablero -> Bool
perteneceListaATablero [y] [] = False
perteneceListaATablero [y] [x]  | [y] == x = True
                   | otherwise = False
perteneceListaATablero [y] (x:xs) | [y] == x = True
                     | otherwise = perteneceListaATablero [y] xs
perteneceListaATablero (y:ys) (x:xs) | (y:ys) == x = True
                        | otherwise = perteneceListaATablero (y:ys) xs


{-devuelveFila :: Tablero -> Fila -> Int
devuelveFila [x] [y]  | pertenece [y] [x] == True = 1
                      | otherwise = 0
devuelveFila (x:xs) [y] | pertenece [y] [x] == True = 1
                        | otherwise = 1 + devuelveFila xs [y]
devuelveFila (x:xs) (y:ys) | pertenece (y:ys) [x] == True =  1
                           | otherwise = 1 + devuelveFila xs (y:ys)

-}
{-valoresDeCamino :: Tablero -> Camino -> [Int]
valoresDeCamino [x] = crearCaminos (aplanar [x])
valoresDeCamino (x:xs) -}