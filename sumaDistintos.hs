{-Dados tres números enteros, calcula la suma sin sumar repetidos (si los hubiera).-}
sumaDos :: Integer -> Integer -> Integer
sumaDos x y | x /= y = x+y
            | otherwise = x

sumaDistintos :: Integer -> Integer -> Integer -> Integer
sumaDistintos x y z = sumaDos (sumaDos x y) z