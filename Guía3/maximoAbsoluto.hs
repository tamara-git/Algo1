{-devuelve el máximo entre el valor absoluto de dos números enteros.-}z
absoluto :: Integer -> Integer
absoluto x  | x < 0 = -x
            | x >= 0 = x

maximo2 :: Integer -> Integer -> Integer
maximo2 x y | x >= y = x
           | otherwise = y  


maximoAbsoluto :: Integer -> Integer -> Integer
maximoAbsoluto x y = maximo2 (absoluto x) (absoluto y) 