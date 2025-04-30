{- ordenar :: [Integer] -> [Integer] que ordena los elementos de la lista en forma creciente. Sugerencia: Pensar
cómo pueden usar la función mínimo para que ayude a generar la lista ordenada necesaria.
-}

minimo :: [Integer] -> Integer
minimo [x] = x
minimo (x:xs) | x <= minimo xs = x
              | otherwise = minimo (xs)  

quitar :: (Eq t) => t -> [t] -> [t]
quitar x [] = []
quitar x (xs) | xs == [x] = []
              | head (xs) /= x = (xs)
              | otherwise = quitar x (tail xs) 

ordenar :: [Integer] -> [Integer]
ordenar [] = []
ordenar [x] = [x]
ordenar (x:xs) | minimo (x:xs) : ordenar (quitar (minimo (x:xs)) (x:xs))