impar :: Integer -> Integer
impar x = 2x - 1

sumaImpares :: Integer -> Integer
sumaImpares x | x == 1 = 1
              | otherwise = sumaImpares (x-1) + impar x

