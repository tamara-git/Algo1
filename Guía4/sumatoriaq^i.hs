sumatoriaqn :: Float -> Integer -> Float
sumatoriaqn q n | n == 1 = q 
                | otherwise = sumatoriaqn q (n-1) + q^n
