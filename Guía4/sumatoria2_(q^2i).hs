sumatoria2_q2n :: Float -> Integer -> Float
sumatoria2_q2n q n | n == 0 = 1
                   | otherwise = sumatoria2_q2n q (2*(n-1)) + q^(2*n)