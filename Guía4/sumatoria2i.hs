sumatoria2i :: Integer -> Integer -> Integer
sumatoria2i 2 i | 2^0 == 1 = 1
                | otherwise = sumatoria2i 2 (i-1) + 2^n
