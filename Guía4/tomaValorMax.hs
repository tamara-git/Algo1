{-Especificar e implementar la función tomaValorMax :: Integer -> Integer -> Integer
 que dado un número entero n1 >= 1, n2 >= n1 tal que sumaDivisores(m) = max{sumaDivisores(i)
 tal que n1 <= i <= n2 -}

sumaDivisoresAux :: Integer -> Integer -> Integer
sumaDivisoresAux m i | (i <= m) && mod m i /= 0 = 0 + sumaDivisoresAux m (i+1)
                     | (i <= m) && (mod m i == 0) = i + sumaDivisoresAux m (i+1)
                     | otherwise = 0

sumaDivisores :: Integer -> Integer
sumaDivisores m = sumaDivisoresAux m 1

maximo :: Integer -> Integer -> Integer
maximo a b | a >= b = a
           | otherwise = b

secuenciaDeMaximos :: Integer -> Integer -> [Integer]
secuenciaDeMaximos n1 n2 | n1 <= n2 = [sumaDivisores(n1)] ++ secuenciaDeMaximos (n1 + 1) n2 
                         | otherwise = [] 
                         
maximoEnSecuencia :: [Integer] -> Integer
maximoEnSecuencia [x] = x
maximoEnSecuencia (x:xs) | x > maximoEnSecuencia xs = x
                         | otherwise = maximoEnSecuencia xs  

tomaValorMax :: Integer -> Integer -> Integer
tomaValorMax n1 n2 = maximoEnSecuencia (secuenciaDeMaximos n1 n2)
