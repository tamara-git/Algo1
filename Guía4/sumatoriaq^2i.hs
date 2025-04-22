sumatoriaq2n :: Integer -> Integer -> Integer
sumatoriaq2n |  n == 1 = q^2
             | otherwise = sumatoriaqn q (2n-2) + q^2n