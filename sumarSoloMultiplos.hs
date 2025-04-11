{-Dada una terna de números enteros y un natural, calcula la suma de los elementos de la terna que son 
múltiplos del número natural.-}
esMultiploDe :: Integer -> Integer -> Bool
esMultiploDe x y = mod x y == 0

sumarSoloMultiplos :: (Integer, Integer, Integer) -> Integer -> Integer
sumarSoloMultiplos (a,b,c) d  | esMultiploDe a d = a
                              | esMultiploDe b d = b
                              | esMultiploDe c d = c
                              | a && b = a+b
                              | a && c = a+c
                              | b && c = b+c
                              | otherwise = 0
