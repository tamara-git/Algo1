{-asegura: el resultado es un número positivo-}
absoluto x :: Integer -> Integer
absoluto x == -x | x < 0
absoluto x == x  | x >= 0