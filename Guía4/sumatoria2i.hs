sumatoria2i :: Integer -> Integer -> Integer
sumatoria2i 2 n | n == 0 = 1 
                | otherwise = sumatoria2i 2 (n-1) + 2^n
