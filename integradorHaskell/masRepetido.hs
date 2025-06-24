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

--Aplano el tablero a una sola lista con todos sus elementos.
aplanar :: Tablero -> Fila
aplanar [] = []
aplanar [x] = x
aplanar (x:xs) = x ++ aplanar xs


cantidadDeApariciones :: Int -> Fila -> Int
cantidadDeApariciones e [x] | e == x = 1
                            | otherwise = 0
cantidadDeApariciones e (x:xs) |  e == x  = 1 + cantidadDeApariciones e xs
                               | otherwise = cantidadDeApariciones e xs 

masRepetidoAux :: Fila -> Int
masRepetidoAux [x] = x
masRepetidoAux (x:xs) | cantidadDeApariciones x (x:xs) > cantidadDeApariciones (masRepetidoAux xs) (x:xs) = x
                      | otherwise = masRepetidoAux xs


masRepetido :: Tablero -> Int
masRepetido (x:xs) = masRepetidoAux (aplanar(x:xs)) 