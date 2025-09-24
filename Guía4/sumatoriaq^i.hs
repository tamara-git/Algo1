{- f2(n,q) = sumatoria desde i=0 hasta n de q^i -}

f2 :: Float -> Integer -> Float
f2 q 1 = q
f2 q n = f2 q (n-1) + q^n