sumatoriaq2n :: Float -> Integer -> Float
sumatoriaq2n q 2n |  n == 1 = q^2
                  | otherwise = sumatoriaqn q (2n-2) + q^2n