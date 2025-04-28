maximo :: [Integer] -> Integer
maximo [x] = x
maximo (x:xs) | x >= maximo xs = x
              | otherwise = maximo (xs)  