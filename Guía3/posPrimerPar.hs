{-Dada una terna de enteros, devueve la posición del primer número par si es que hay alguno, o devuelve
4 si son todos impares -}

posPrimerPar :: (Integer,Integer,Integer) -> Integer
posPrimerPar (a,b,c) | (mod a 2 == 0) = 1
                     | (mod b 2 == 0) = 2
                     | (mod c 2 == 0) = 3
                     | otherwise = 4
