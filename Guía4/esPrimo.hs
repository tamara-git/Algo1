--Implementar una función que determine si un número es primo, o no.

menorDivisorDesde :: Integer -> Integer -> Integer
menorDivisorDesde x d | mod x d == 0 = d
                      | otherwise = menorDivisorDesde x (d + 1)

menorDivisor :: Integer -> Integer
menorDivisor x = menorDivisorDesde x 2 

esPrimo :: Integer -> Bool 
esPrimo x | menorDivisor x == x = True
          | otherwise = False