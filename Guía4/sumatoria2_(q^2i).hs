--esta sumatoria es la de sumatoriaq^i.hs pero comenzando desde i=0
sumatoriaqn0 :: Float -> Integer -> Float
sumatoriaqn0 q n | n == 0 = 1
                 | n == 1 = 1 + q 
                 | otherwise = sumatoriaqn q (n-1) + q^n

sumatoriaq2n :: Float -> Integer -> Float
sumatoriaq2n q n | n == 0 = 0
                 | n == 1 = (q^2 + q^1)
                 | otherwise = q^(2*n) + q^(2*n-1) + sumatoriaq2n q (n-1)     

sumatoria2_q2n :: Float -> Integer -> Float
sumatoria2_q2n q n | n == 0 = 1
                   | n == 1 == (q^2 + q^1)
                   | otherwise = sumatoriaq2n q n - (sumatoriaqn q (n-1))              