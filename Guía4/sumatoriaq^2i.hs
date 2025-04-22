sumatoriaq2n :: Float -> Integer -> Float
sumatoriaq2n q n | n == 0 = 0
                 | n == 1 = sumatoriaq2n q 2
                 | otherwise = (sumatoriaq2n q (n-2)) + q^(n)