sumatoriaqn :: Float -> Integer -> Float
sumatoriaqn q n | n == 1 = q 
                | otherwise = sumatoriaqn q (n-1) + q^n



sumatoriaq2n :: Float -> Integer -> Float
sumatoriaq2n q n | n == 0 = 0
                 | otherwise = sumatoriaqn q 2*n