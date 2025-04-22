sumatoriaq2n :: Float -> Integer -> Float
sumatoriaq2n q (2*n) | n == 1 = q^2
                   | otherwise = sumatoriaq2n q (2*n-2) + q^(2*n)