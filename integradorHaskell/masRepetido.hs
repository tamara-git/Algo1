{-. Implementar la funci´on masRepetido :: Tablero ->Int
problema masRepetido (t: Tablero) : Z {
requiere: {El tablero t es un tablero bien formado, es decir, la longitud de todas las filas es la misma, y tienen al
menos un elemento}
requiere: {Existe al menos una columna en el tablero t }
requiere: {El tablero t no es vac´ıo, todos los n´umeros del tablero son positivos, mayor estricto a 0}
asegura: {res es igual al n´umero que m´as veces aparece en un tablero t. Si hay empate devuelve cualquiera de ellos}
}-}

type Fila = [Int]
type Tablero = [Fila]


cantidadDeApariciones :: Int -> Fila -> Int
cantidadDeApariciones e (x:xs) | x == e = 1 + cantidadDeApariciones e xs
                               | otherwise = cantidadDeApariciones e xs

cantidadDeAparicionesTablero :: Int -> Tablero -> Int
cantidadDeAparicionesTablero e (x:xs) | cantidadDeApariciones e x > 0 = cantidadDeApariciones e x + cantidadDeAparicionesTablero e xs
                                      | otherwise = cantidadDeAparicionesTablero e xs

mayorCantidadDeApariciones :: Fila -> Int
mayorCantidadDeApariciones (x:xs) | cantidadDeApariciones x xs == 0 = 1 
                                  | otherwise = 1 + cantidadDeApariciones (xs) 


{-masRepetido :: Tablero -> Int
masRepetido [x] | (cantidadDeApariciones e x > cantidadDeApariciones y x) = e
                | otherwise = y
masRepetido (x:xs) | cantidadDeAparicionesTablero e (x:xs) > cantidadDeAparicionesTablero y (x:xs) = e
                   | otherwise = y-}
