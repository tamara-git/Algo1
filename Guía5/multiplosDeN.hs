{- multiplosDeN :: Integer -> [Integer] -> [Integer] que dado un número n y una lista xs, devuelve una lista
con los elementos de xs múltiplos de n.-}

multiplosDeN :: Integer -> [Integer] -> [Integer]
multiplosDeN n [] = []
multiplosDeN n (x:xs) | (mod x n == 0) = x:(multiplosDeN n (xs))
                      | otherwise = multiplosDeN n (xs) 