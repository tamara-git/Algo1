sumatoria2_q2n :: Float -> Integer -> Float
sumatoria2_q2n q 2n | n == 0 = 1
                    | n == 1 = sumatoria2_q2n q 2 
                    | n = 2 = sumatoria2_q2n q 4
                    | otherwise = sumatoria2_q2n q (2*(n-1)) + q^(2*n)