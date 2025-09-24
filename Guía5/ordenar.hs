{- ordenar :: [Integer] -> [Integer] que ordena los elementos de la lista en forma creciente. Sugerencia: Pensar
cómo pueden usar la función maximo para que ayude a generar la lista ordenada necesaria.
-}

maximo :: [Integer] -> Integer 
maximo [x] = x
maximo (x:xs) | x >= maximo xs = x 
              | otherwise = maximo xs

quitar :: Integer -> [Integer] -> [Integer]
quitar x [] = []
quitar x [y] | x == y = []
             | otherwise = [y]
quitar x (y:ys) | x == y = ys 
                | otherwise = y:quitar x ys

ordenar :: [Integer] -> [Integer]
ordenar [] = []
ordenar [x] = [x]
ordenar (x:xs) = ordenar (quitar (maximo(x:xs)) (x:xs)) ++ [maximo (x:xs)]




--Hecho con mínimo
minimo :: [Integer] -> Integer
minimo [] = 0
minimo [x] = x
minimo (x:xs) | x <= minimo xs = x
              | otherwise = minimo (xs)  

ordenar2 :: [Integer] -> [Integer]
ordenar2 [] = []
ordenar2 [x] = [x]
ordenar2 xs = minimo (xs) : ordenar2 (quitar (minimo xs) xs)
