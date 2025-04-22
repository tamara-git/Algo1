sumatoria2_q2n :: Float -> Integer -> Float
sumatoria2_q2n q 2n | n == 0 = 1
                  | n == 1 = sumatoria2_q2n q 2 
                  | otherwise = sumatoria2_q2n q (2n-2) + q^2n