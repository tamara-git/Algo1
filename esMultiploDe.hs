{-Dados dos números naturales, decide si el primero es el múltiplo del segundo-}
esMultiploDe :: Integer -> Integer -> Bool
esMultiploDe x y = (mod x y)
             