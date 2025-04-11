{-Dada una terna de números enteros y un natural, calcula la suma de los elementos de la terna que son 
múltiplos del número natural.-}
esMultiploDe :: Integer -> Integer -> Integer
esMultiploDe x y | mod x y == 0 = x
                 | otherwise = 0
                 

sumarSoloMultiplos :: (Integer, Integer, Integer) -> Integer -> Integer
sumarSoloMultiplos (a,b,c) d  | esMultiploDe a d + esMultiploDe b d + esMultiploDe c d 

                              
                            
