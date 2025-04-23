{-Especificar e implementar una función eAprox :: Integer ->Float que aproxime el valor del número e
a partir de la siguiente sumatoria:
eˆ(n) = sumatoria i=0 n  de 1/i!
-}
-- Intento hacer la recursión en 
factorial :: Integer -> Integer
factorial x | x == 0 = 1
            | otherwise = x * factorial (x-1)

e_aprox :: Integer -> Float
e_aprox x  | x == 0 = 1.0
           | x == 1 = 2.0
           | otherwise = (factorial x)**(-1) + e_aprox (x-1)
            