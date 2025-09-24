{- f1(n) = sumatoria desde i=0 hasta n de 2^i -}
f1 :: Integer -> Integer
f1 0 = 1
f1 1 = f1 0 + 2 
f1 n = f1 (n-1) + 2^n