{-Especificar e implementar la función esDivisible :: Integer ->Integer ->Bool 
que dados dos números naturales determina si el primero es divisible por el segundo. 
No está permitido utilizar las funciones mod ni div.-}

siEsMultiploDevuelveN :: Integer -> Integer -> Integer
siEsMultiploDevuelveN n m | n < m = 0
                          | otherwise = m + siEsMultiploDevuelveN (n-m) m 


esDivisible :: Integer -> Integer -> Bool
esDivisible n m | siEsMultiploDevuelveN n m == n = True
                | otherwise = False