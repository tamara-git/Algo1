sumatoriaqn :: Integer-> Integer -> Integer
sumatoriaqn q n | n == 1 = q 
                | otherwise = sumatoriaqn q (n-1) + q^n
