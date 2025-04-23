{-Especificar e implementar una función eAprox :: Integer ->Float que aproxime el valor del número e
a partir de la siguiente sumatoria:
eˆ(n) = sumatoria i=0 n  de 1/i!
-}
-- Use fromInteger para convertir x en Float
factorial :: Integer -> Float
factorial x | x == 0 = 1
            | otherwise = fromInteger x * factorial (x-1)

e_aprox :: Integer -> Float
e_aprox x  | x == 0 = 1
           | x == 1 = 2
           | otherwise = (factorial x)**(-1) + e_aprox (x-1)

{- b) Definir la constante e :: Float como la aproximación de e a partir de los primeros
10 términos de la serie anterior.-}
--Obs: me conviene usar fromIntegral para convertir UNA FUNCIÓN Integer en Float y no simplemente un valor.

e :: Float 
e = fromIntegral (e_aprox 10)
            