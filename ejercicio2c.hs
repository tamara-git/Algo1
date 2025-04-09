maximo2 :: Integer -> Integer -> Integer
maximo2 x y | (x >= y) = x
            | otherwise = y
      

maximo3 :: Integer -> Integer -> Integer -> Integer
maximo3 x y z | (maximo2 >= z) = maximo2
              | otherwise = z