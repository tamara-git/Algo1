sumatoriaqn :: Float -> Integer -> Float
sumatoriaqn q n | n == 1 = q 
                | otherwise = sumatoriaqn q (n-1) + q^n

sumatoria2_q2n :: Float -> Integer -> Float
sumatoria2_q2n q n | n == 0 = 1
                   | n == 1 == (q^2 + q^1)
                   | otherwise = q^(2*n) + q^(n-1)+ sumatoria2_q2n q (n-1) - sumatoriaqn q (n-1)