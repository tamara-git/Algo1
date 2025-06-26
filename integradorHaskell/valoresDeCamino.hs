{-Implementar la funci´on valoresDeCamino :: Tablero -> Camino ->[Int]
problema valoresDeCamino (t: Tablero, c: Camino) : seq⟨Z⟩ {
requiere: {El tablero t es un tablero bien formado, es decir, la longitud de todas las filas es la misma, y tienen al
menos un elemento}
requiere: {Existe al menos una columna en el tablero t }
requiere: {El tablero t no es vac´ıo, todos los n´umeros del tablero son positivos, mayores estrictos a 0}
requiere: {El camino c es un camino válido, es decir, secuencia de posiciones adyacentes en la que solo es posible
desplazarse hacia la posici´on de la derecha o hacia abajo y todas las posiciones est´an dentro de los limites del tablero
t}
asegura: {res es igual a la secuencia de n´umeros que est´an en el camino c, ordenados de la misma forma que aparecen
las posiciones correspondientes en el camino.}
}-}
{-Fila = seq⟨Z⟩
Tablero = seq⟨Fila⟩
Posicion = Z × Z – Observaci´on: las posiciones son: (fila, columna)
Camino = seq⟨Posicion⟩-}

type Fila = [Int]
type Tablero = [[Int]]
type Camino = [(Int,Int)]


aplanar :: Tablero -> [Int]
aplanar [x] = x
aplanar (x:xs) = x ++ aplanar xs


--Cantidad de filas que tiene el tablero. 
filas :: Tablero -> Int
filas [x] = 1
filas (x:xs) = 1 + (filas xs)


--Cantidad de columnas que tiene el tablero.
columnas :: [Int] -> Int 
columnas [x] = 1
columnas (x:xs) = 1 + (columnas xs)


posicion :: Int -> [Int] -> Int
posicion e [x] | e == x = 1
posicion e (x:xs) | e == x = 1 
                  | otherwise = 1 + posicion e xs


posicionFila ::  Fila -> Int -> Int -> [(Int,Int)]
posicionFila [] 1 1 = [] 
posicionFila [x] n m = [(n, 0+m)] 
posicionFila (x:xs) n m = [(n, 0+m)] ++ posicionFila xs n (m+1)


posicionTablero :: Tablero -> Int -> [(Int,Int)]
posicionTablero [x] n = posicionFila x n 1
posicionTablero (x:xs) n = posicionFila x n 1 ++ posicionTablero xs (n+1)    


matrizPosiciones :: Tablero -> [(Int,Int)]
matrizPosiciones [x] = posicionTablero [x] 1
matrizPosiciones (x:xs) = posicionTablero (x:xs) 1
                   