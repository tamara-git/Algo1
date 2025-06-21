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

pertenece :: Int -> Fila -> Bool
pertenece e (x:xs) | e == x = True
                   | otherwise = pertenece e xs

perteneceTablero :: Int -> Tablero -> Bool
perteneceTablero e (x:xs) | pertenece e x = True
                          | otherwise = perteneceTablero e xs

cantidadDeApariciones :: Int -> Fila -> Int
cantidadApariciones e [x] | e == x = 1
                          | otherwise = 0
cantidadDeApariciones e (x:xs) |  e == x  = 1 + cantidadDeApariciones e xs
                               | otherwise = cantidadDeApariciones e xs 

cantidadAparicionesTablero :: Int -> Tablero -> Int
cantidadAparicionesTablero e (x:xs) | cantidadApariciones e x > 0 = cantidadApariciones e x + cantidadAparicionesTablero e xs
                                    | otherwise = cantidadAparicionesTablero e xs

tuplasNumeroConAparicion :: Fila -> [(Int, Int)] 
tuplasNumeroConAparicion [x] = [(x, 1)]
tuplasNumeroConAparicion (x:xs) | cantidadApariciones x xs == 0 = [(x,1)]
                                | otherwise = [(x, 1 + cantidadApariciones x xs)] 

