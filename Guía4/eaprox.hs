{-Especificar e implementar una función eAprox :: Integer ->Float que aproxime el valor del número e
a partir de la siguiente sumatoria:
eˆ(n) = sumatoria i=0 n  de 1/i!
-}
-- Use fromInteger para convertir x en Float


factorial :: Integer -> Integer
factorial 0 = 1
factorial 1 = 1
factorial n = n * factorial (n-1)

eAprox :: Integer -> Float
eAprox 0 = 1 
eAprox 1 = 1 + 1 / fromInteger (factorial 1)
eAprox n = eAprox (n-1) +  1 / fromInteger (factorial n)


{- b) Definir la constante e :: Float como la aproximación de e a partir de los primeros
10 términos de la serie anterior.-}
--Obs final: me conviene usar fromIntegral para convertir UNA FUNCIÓN Integer en Float y no simplemente un valor.

e :: Float
e = eAprox 10        