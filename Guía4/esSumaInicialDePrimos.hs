esPrimo :: Integer -> Bool
esPrimo n | menorDivisor n == n = True
          | otherwise = False


menorDivisorDesde :: Integer -> Integer -> Integer
menorDivisorDesde n desde | mod n desde == 0 = desde
                          | otherwise = menorDivisorDesde n (desde + 1) 

menorDivisor :: Integer -> Integer
menorDivisor n = menorDivisorDesde n 2



esSumaInicialDePrimos :: 