{-Fila = seq⟨Z⟩
Tablero = seq⟨F ila⟩
Posicion = Z × Z – Observaci´on: las posiciones son: (fila, columna)
Camino = seq⟨Posicion⟩-}

{-Implementar la funci´on maximo :: Tablero ->Int
problema maximo (t: Tablero) : Z {
requiere: {El tablero t es un tablero bien formado, es decir, la longitud de todas las filas es la misma, y tienen al
menos un elemento}
requiere: {Existe al menos una columna en el tablero t }
requiere: {El tablero t no es vac´ıo, todos los n´umeros del tablero son positivos, mayor estricto a 0}
asegura: {res es igual al n´umero m´as grande del tablero t}
}-}

type Fila = [Int]
type Tablero = [Fila]
-- [[1,2,3],[3,4,5]]

maximoFila :: Fila -> Int
maximoFila [x] = x
maximoFila (x:xs) | x > maximoFila xs = x
                  | otherwise = maximoFila xs

maximo :: Tablero -> Int
maximo x = maximoFila x
maximo (x:xs) | maximoFila x > maximo xs = maximoFila x
              | otherwise = maximo xs

              
