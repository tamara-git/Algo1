{-problema sumaImpares (x: Z) : Z {
requiere: { x ≥ 1 }
asegura: { resultado = sumatoria i=1 n (2n-1) }
} 
-}

impar :: Integer -> Integer
impar x = 2*x - 1

sumaImpares :: Integer -> Integer
sumaImpares x | x == 1 = 1
              | otherwise = sumaImpares (x-1) + impar x

