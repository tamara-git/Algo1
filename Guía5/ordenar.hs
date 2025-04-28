minimo :: [Integer] -> Integer
minimo [x] = x
minimo (x:xs) | x <= minimo xs = x
              | otherwise = minimo (xs)  

ordenar :: [Integer] -> [Integer]
ordenar [x] = [x]
ordenar (x:xs) |  x <= minimo xs = [x] ++ [minimo (xs)]
               | otherwise = [minimo (xs)] ++ [x]