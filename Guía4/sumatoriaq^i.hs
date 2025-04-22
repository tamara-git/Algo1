sumatoriaqn :: Float -> Integer -> Float
sumatoriaqn q n | n == 0 = 0
                | n == 1 = q 
                | otherwise = (sumatoria2_q2n q (2*(n-1))) + q^(2*n)
