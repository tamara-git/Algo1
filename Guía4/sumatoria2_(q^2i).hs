{- f4(n,q) = sumatoria desde i=n hasta 2n de q^i 
requiere : {n >= 0  ^  q pertenece a los reales} -}
f4 :: Float -> Integer -> Float
f4 q 0 = 1 
f4 q 1 = q^2 + q 
f4 q n = q^2n + q^(2*n-1) + f4 q (n-1) - q^(n-1)