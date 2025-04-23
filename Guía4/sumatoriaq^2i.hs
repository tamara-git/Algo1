sumatoriaq2n :: Float -> Integer -> Float
sumatoriaq2n q n | n == 0 = 0
                 | n == 1 = (q^2 + q^1)
                 | otherwise = q^(2*n) + q^(2*n-1) + sumatoria2_q2n q (n-1)            