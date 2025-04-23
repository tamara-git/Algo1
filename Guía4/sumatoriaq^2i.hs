sumatoriaq2n :: Float -> Integer -> Float
sumatoriaq2n q n | n == 0 = 0
                 | n == 1 = (q^2 + q^1)
                  n == 2 = q^4 + q^3 +      q^2    
                  n == 3 = q^6 + q^5  +      q^4 + q^3
                 | otherwise = 
                 