{- ordenar :: [Integer] -> [Integer] que ordena los elementos de la lista en forma creciente. Sugerencia: Pensar
cómo pueden usar la función mínimo para que ayude a generar la lista ordenada necesaria.
-}

minimo :: [Integer] -> Integer
minimo [x] = x
minimo (x:xs) | x <= minimo xs = x
              | otherwise = minimo (xs)  

ordenar :: [Integer] -> [Integer]
ordenar [] = []
ordenar [x] = [x]
ordenar (x:xs) | x <= minimo xs = x (x:minimo (xs):xs)
               | otherwise = ordenar (xs)