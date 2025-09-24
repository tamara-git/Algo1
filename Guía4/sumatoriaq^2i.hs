{-f3(n,q) = sumatoria desde i=1 hasta 2n de q^i -}
f3 :: Float -> Integer -> Float
f3 q 1 = q + q^2
f3 q n = q^(2*n) + q^(2*n-1) + f3 q (n-1)