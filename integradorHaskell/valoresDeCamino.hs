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


indiceColumna :: Fila -> Int -> Int
indice [x] e | e == x = 1 
indice (x:xs) e | e == x = 1
                | otherwise = 1 + indice xs e


indiceFila :: Tablero -> [Int] -> Int
indiceFila [x] fila | fila == x = 1
                    | otherwise = 0
indiceFila (x:xs) fila | fila == x = 1
                       | otherwise = 1 + indiceFila xs fila


perteneceAFila :: Int -> [Int] -> Bool
perteneceAFila e [x] | e == x = True
                     | otherwise = False
perteneceAFila e (x:xs) | e == x = True
                        | otherwise = perteneceAFila e xs


posicionElemento :: Tablero -> Int -> (Int,Int)
posicionElemento [x] e =  (indiceFila [x] x, indiceColumna x e)
posicionElemento (x:xs) e | perteneceAFila e x == True = (indiceFila (x:xs) x, indiceColumna x e)
                          | otherwise = posicionElemento xs e