menorDivisorDesde :: Integer -> Integer -> Integer
menorDivisorDesde n desde | mod n desde == 0 = desde
                          | otherwise = menorDivisorDesde n (desde + 1)

menorDivisor :: Integer -> Integer
menorDivisor n = menorDivisorDesde n 2

esPrimo :: Integer -> Bool
esPrimo n | menorDivisor n == n = True
          | otherwise = False

secuenciaDePrimos :: Integer -> Integer -> [Integer]
secuenciaDePrimos desde hasta | (desde <= hasta) && (esPrimo desde == False) = [] ++ secuenciaDePrimos (desde + 1) hasta  
                              | (desde <= hasta) && (esPrimo desde == True) = [desde] ++ secuenciaDePrimos (desde + 1) hasta  
                              | otherwise = [] 

longitudLista :: [Integer] -> Integer
longitudLista [] = 0
longitudLista [x] = 1
longitudLista (x:xs) = 1 + longitudLista xs  


primoEnPosicion :: Integer -> [Integer] -> Integer
primoEnPosicion 1 [x] = x
primoEnPosicion 1 (x:xs) = x
primoEnPosicion i (x:xs) = primoEnPosicion (i-1) xs


nEsimoPrimoAux :: Integer -> Integer -> Integer
nEsimoPrimoAux n hasta | longitudLista (secuenciaDePrimos 2 hasta) >= n = primoEnPosicion n (secuenciaDePrimos 2 hasta)
                       | otherwise = 0 + nEsimoPrimoAux n (hasta + 1)

nEsimoPrimo :: Integer -> Integer
nEsimoPrimo n = nEsimoPrimoAux n 2