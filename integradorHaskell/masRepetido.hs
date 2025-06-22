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
masRepetidoAux (x:xs) | cantidadDeApariciones x (x:xs) > masRepetidoAux xs = x
                      | otherwise = masRepetidoAux xs












{-pertenece :: Int -> Fila -> Bool
pertenece e (x:xs) | e == x = True
                   | otherwise = pertenece e xs


tuplasNumeroConAparicion :: Fila -> [(Int, Int)] 
tuplasNumeroConAparicion [x] = [(x, 1)]
tuplasNumeroConAparicion (x:xs) | cantidadDeApariciones x xs == 0 = [(x,1)] ++ tuplasNumeroConAparicion xs
                                | otherwise = [(x, 1 + cantidadDeApariciones x xs)] ++ tuplasNumeroConAparicion xs

tuplasNumeroConAparicionSinRepetidos :: Fila -> [(Int, Int)]
tuplasNumeroConAparicionSinRepetidos [x] = tuplasNumeroConAparicion [x]
tuplasNumeroConAparicionSinRepetidos (x:xs) = eliminarTuplasConFstRepetidas (tuplasNumeroConAparicion (x:xs))

tuplasNumeroConAparicionTablero :: Tablero -> [(Int, Int)] 
tuplasNumeroConAparicionTablero [x] = tuplasNumeroConAparicionSinRepetidos x
tuplasNumeroConAparicionTablero (x:xs)  |  tuplasNumeroConAparicionSinRepetidos x ++ tuplasNumeroConAparicionTablero xs

tuplasNroConAparicionTableroSinRepe :: [(Int,Int)] -> [(Int,Int)]
tuplasNroConAparicionTableroSinRepe [x] = tuplasNumeroConAparicionTablero [x]
tuplasNroConAparicionTableroSinRepe (x:xs) | sumarSndDeTuplasIgualFst 




sumarSndDeTuplasIgualFst :: [(Int, Int)] -> [(Int,Int)]
sumarSndDeTuplasIgualFst [x]
sumarSndDeTuplasIgualFst (x:xs) | 

perteneceFst :: Int ->  [(Int,Int)] -> Bool
perteneceFst a [x] | fst x == a = True 
                   | otherwise = False
perteneceFst a (x:xs) | fst x == a = True 
                      | otherwise = perteneceFst a xs

eliminarTupla :: Int -> [(Int,Int)] -> [(Int,Int)]
eliminarTupla a [] = []
eliminarTupla a [x] | fst x == a = []
eliminarTupla a (x:xs) | fst x == a = eliminarTupla a xs
                       | otherwise = x: eliminarTupla a xs 

eliminarTuplasConFstRepetidas :: [(Int,Int)] -> [(Int,Int)]
eliminarTuplasConFstRepetidas [] = []
eliminarTuplasConFstRepetidas [x] = [x]
eliminarTuplasConFstRepetidas (x:xs) | perteneceFst (fst x) xs == True = [x] ++ eliminarTuplasConFstRepetidas (eliminarTupla (fst x) xs)
                                     | otherwise =  [x] ++ eliminarTuplasConFstRepetidas xs-}