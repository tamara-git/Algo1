maximo :: [Integer] -> Integer
maximo [x] = x
maximo (x:xs) | x >= xs = x
              | otherwise = maximo (xs)  