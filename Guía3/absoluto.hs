{-calcula el valor absoluto de un número entero-}
absoluto :: Integer -> Integer
absoluto x  | x >= 0 = x
            | otherwise = -x