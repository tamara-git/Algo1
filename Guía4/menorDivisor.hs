{-Implementar menorDivisor :: Integer -> Integer que calcule el menor divisor (mayor que 1)
 de un natural n pasado como parámetro.
-}
--Mio

menorDivisorDesde :: Integer -> Integer -> Integer
menorDivisorDesde n d | (d <= n) && (mod n d == 0) = d 
                      | (d <= n) && (mod n d /= 0) = menorDivisorDesde n (d+1)


menorDivisor :: Integer -> Integer
menorDivisor n = menorDivisorDesde n 2


{-
--Clase
--requiere desde < n
menorDivisorDesde :: Integer -> Integer -> Integer
menorDivisorDesde n desde | mod n desde == 0 = desde
                          | otherwise = menorDivisorDesde n (desde + 1) 

menorDivisor :: Integer -> Integer
menorDivisor n = menorDivisorDesde n 2
               -}