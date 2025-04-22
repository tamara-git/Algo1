sumatoria2i :: Integer -> Integer -> Integer
sumatoria2i 2 i | i == 0 = 2^1 
                | otherwise = sumatoria2i 2 (i-1) + 2^i
