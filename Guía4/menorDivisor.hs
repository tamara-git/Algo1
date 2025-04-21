--Mio
esdivisor :: Integer -> Integer -> Integer
esdivisor n i | mod (n i) == 0 = div n i 
              | otherwise = 

menorDivisor :: Integer -> Integer
menorDivisor n | 
               | 

esdivisor n m < esdivisor n i


--Clase
--requiere desde < n
menorDivisorDesde :: Integer -> Integer -> Integer
menorDivisorDesde n desde | mod n desde == 0 = desde
                          | otherwise = menorDivisorDesde n (desde + 1) 

menorDivisor :: Integer -> Integer
menorDivisor n = menorDivisorDesde n 2
               