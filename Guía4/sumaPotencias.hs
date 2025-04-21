{-
    requiere: {True}
    asegura: {res = sumatoria i=1 n (sumatoria j=1 m  q^(i+j)) }
-}

sumatoriaInterna :: Integer -> Integer -> Integer -> Integer
sumatoriaInterna q n m  | m == 1 = q^(n+m)
                        | otherwise = q^(n+m) + sumatoriaInterna q n (m-1)

sumaPotencias :: Integer -> Integer -> Integer -> Integer
sumaPotencias q n m | n == 1 = sumatoriaInterna q n m
                    | otherwise = sumatoriaInterna q n m + sumaPotencias q (n-1) m 