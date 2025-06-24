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

perteneceListaATablero :: [Int] -> Tablero -> Bool
perteneceListaATablero [] [] = False
perteneceListaATablero [y] [] = False
perteneceListaATablero [] [x] = False
perteneceListaATablero [y] [x]  | todosElementosIguales [y] x == True = True 
                                | otherwise = False
perteneceListaATablero (y:ys) [] = False
perteneceListaATablero [] (x:xs) = False
perteneceListaATablero [y] (x:xs) | todosElementosIguales [y] x == True = True
                                  | otherwise = perteneceListaATablero [y] xs
perteneceListaATablero (y:ys) (x:xs) | todosElementosIguales (y:ys) x == True = True
                                     | otherwise = perteneceListaATablero (y:ys) xs


devuelveFila :: Tablero -> Fila -> Int
devuelveFila [x] [y]  | perteneceListaATablero [y] [x] == True = 1
                      | otherwise = 0
devuelveFila (x:xs) [y] | perteneceListaATablero [y] [x] == True = 1
                        | otherwise = 1 + devuelveFila xs [y]
devuelveFila (x:xs) (y:ys) | perteneceListaATablero (y:ys) [x] == True =  1
                           | otherwise = 1 + devuelveFila xs (y:ys)

armarListaColumna :: Tablero -> [Int]
armarListaColumna [x] = [head x]
armarListaColumna (x:xs) = [head x] + armarListaColumna xs

perteneceColumnaATablero :: [Int] -> Tablero -> Bool
perteneceColumnaATablero [] [] = False
perteneceColumnaATablero [y] [] = False
perteneceColumnaATablero [] [x] = False
perteneceColumnaATablero (y:ys) [] = False
perteneceColumnaATablero [] (x:xs) = False
perteneceColumnaATablero [y] [x]  | head x == y = True
                                  | otherwise = False
perteneceColumnaATablero (y:ys) (x:xs) | head x == y = perteneceColumnaATablero ys xs
                                       | otherwise = False


{-devuelveColumna :: Tablero -> [Int] -> Int
devuelveColumna [x] y | perteneceColumnaATablero [y] [x] == True = 1
                        | otherwise = 0
devuelveColumna [x] y:ys | perteneceColumnaATablero [x] (y:ys) == True = 
                           | otherwise = 0
-}

{-posicion ::  Tablero -> Int -> Int
posicion [x] e = devuelveFila [x] x
posicion [x] 
--posicion (x:xs) e | (devuelveFila (x:xs) , devuelveColumna)

-}
{-valoresDeCamino :: Tablero -> Camino -> [Int]
valoresDeCamino [x] [(a,b)] = devuelveFila (x:xs)
valoresDeCamino (x:xs) [(a,b)] -}