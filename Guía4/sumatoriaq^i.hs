sumatoriaqn :: Integer-> Integer -> Integer
sumatoriaqn q n | n == 0 = 1 
                | otherwise = sumatoriaqn q (n-1) + q^n
