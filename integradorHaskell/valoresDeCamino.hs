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


accederAElementoPorIndice :: Fila -> Int -> Int 
accederAElementoPorIndice [x] 1 = x 
accederAElementoPorIndice (x:xs) 1 = x 
accederAElementoPorIndice (x:xs) n = accederAElementoPorIndice xs (n-1)

fila :: Tablero -> Int -> Fila 
fila [x] 1 = x
fila (x:xs) 1 = x
fila (x:xs) n = fila xs (n-1)


posicionTablero :: Tablero -> (Int,Int) -> Int -> Int
posicionTablero [x] (a,b) = accederAElementoPorIndice (fila [x] a) b
posicionTablero (x:xs) (a,b) = accederAElementoPorIndice (fila (x:xs) a) b
                          