sumatoria2i :: Integer -> Integer -> Integer
sumatoria2i n i | 2^0 == 1 = 1
                | otherwise = sumatoria2i n (i-1) + 2^n
