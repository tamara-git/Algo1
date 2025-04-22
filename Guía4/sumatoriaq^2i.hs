sumatoriaq2n :: Float -> Integer -> Float
sumatoriaq2n q n | n == 0 = 0
                 | n == 1 = (q^1 + q^2)
                 | otherwise = (sumatoriaq2n q (2*(n-1))) + q^(2*n)