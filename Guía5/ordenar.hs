{- ordenar :: [Integer] -> [Integer] que ordena los elementos de la lista en forma creciente. Sugerencia: Pensar
c´omo pueden usar la funci´on m´ınimo para que ayude a generar la lista ordenada necesaria.
-}

minimo :: [Integer] -> Integer
minimo [x] = x
minimo (x:xs) | x <= minimo xs = x
              | otherwise = minimo (xs)  

ordenar :: [Integer] -> [Integer]
ordenar [] = []
ordenar [x] = [x]
ordenar (x:xs) | x <= minimo (xs) = (x:minimo(xs))
               | otherwise = [minimo(xs)]
