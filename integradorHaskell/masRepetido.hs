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
type Tupla = (Int,Int)

cantidadDeApariciones :: Int -> Fila -> Int
cantidadDeApariciones e [x] | e == x = 1
                            | otherwise = 0
cantidadDeApariciones e (x:xs) | x == e = 1 + cantidadDeApariciones e xs
                               | otherwise = cantidadDeApariciones e xs

cantidadDeAparicionesTablero :: Int -> Tablero -> Tupla
cantidadDeAparicionesTablero e [x] | cantidadDeApariciones e x == 0 = ()
cantidadDeAparicionesTablero e (x:xs) | cantidadDeApariciones e x > 0 = (e,cantidadDeApariciones e x + cantidadDeAparicionesTablero e xs)
                                      | otherwise = (e,cantidadDeAparicionesTablero e xs)



{-mayorCantidadDeApariciones :: Fila -> Int
mayorCantidadDeApariciones [x] = 1
mayorCantidadDeApariciones (x:xs) | cantidadDeApariciones 
                                  | otherwise = 1 + mayorCantidadDeApariciones xs-}

{-masRepetido :: Tablero -> Int
masRepetido [x] | cantidadDeApariciones (head x) > cantida
masRepetido (x:xs) | cantidadDeAparicionesTablero e (x:xs) > cantidadDeAparicionesTablero y (x:xs) = e
                   | otherwise = y
-}