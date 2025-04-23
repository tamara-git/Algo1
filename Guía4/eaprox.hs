{-Especificar e implementar una función eAprox :: Integer ->Float que aproxime el valor del número e
a partir de la siguiente sumatoria:
eˆ(n) = sumatoria i=0 n  de 1/i!
-}
e_aprox :: Integer -> Float
e_aprox x  | x == 0 = 1
           | x == 1 = 1
           | otherwise = div (1 x!) + e_aprox (x-1)