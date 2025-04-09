{-asegura: el resultado es un número positivo-}
 x :: Integer -> Integer
absoluto x == -x | x < 0
absoluto x == x  | x >= 0