sumatoriaqn :: Float -> Integer -> Float
sumatoriaqn q n | n == 1 = q 
                | otherwise = sumatoriaqn q (n-1) + q^n

sumatoriaq2n :: Float -> Integer -> Float
sumatoriaq2n q n | n == 0 = 0
                 | n == 1 = (q^2 + q^1)
                 | otherwise = q^2*n + q^(2*n-1) + sumatoriaq2n q (n-1)