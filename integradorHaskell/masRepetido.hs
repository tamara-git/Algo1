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
cantidadDeApariciones e [] = 0
cantidadDeApariciones e [x] | e == x = 1
                          | otherwise = 0
cantidadDeApariciones e (x:xs) |  e == x  = 1 + cantidadDeApariciones e xs
                               | otherwise = cantidadDeApariciones e xs 

cantidadAparicionesTablero :: Int -> Tablero -> Int
cantidadAparicionesTablero e (x:xs) | cantidadDeApariciones e x > 0 = cantidadDeApariciones e x + cantidadAparicionesTablero e xs
                                    | otherwise = cantidadAparicionesTablero e xs


tuplasNumeroConAparicion :: Fila -> [(Int, Int)] 
tuplasNumeroConAparicion [x] = [(x, 1)]
tuplasNumeroConAparicion (x:xs) | cantidadDeApariciones x xs == 0 = [(x,1)] ++ tuplasNumeroConAparicion xs
                                | otherwise = (x, [(x, 1 + cantidadDeApariciones x xs)] ++ tuplasNumeroConAparicion xs)


perteneceFst :: Int ->  [(Int,Int)] -> Bool
perteneceFst a (x:xs) | fst x == a = True 
                      | otherwise = perteneceFst a xs

eliminarTupla :: Int -> [(Int,Int)] -> [(Int,Int)]
eliminarTupla a [] = []
eliminarTupla a [x] | fst x == a = []
eliminarTupla a (x:xs) | fst x == a = eliminarTupla a xs
                       | otherwise = x: eliminarTupla a xs 

eliminarTuplasConFstRepetidas :: [(Int,Int)] -> [(Int,Int)]
eliminarTuplasConFstRepetidas (x:xs) | perteneceFst (fst x) xs == True = eliminarTupla (fst x) xs
                                     | otherwise = [x] ++ eliminarTuplasConFstRepetidas xs