{-problema sumaImpares (x: Z) : Z {
requiere: { x ≥ 1 }
asegura: { resultado = sumatoria i=1 n (2n-1) }
} 
-}

impar :: Integer -> Integer
impar n = 2*n - 1

sumaImpares :: Integer -> Integer
sumaImpares x = impar x + sumaImpares (x-1)