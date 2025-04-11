{-Dada una terna de números enteros y un natural, calcula la suma de los elementos de la terna que son 
múltiplos del número natural.-}
esMultiploDe :: Integer -> Integer -> Bool
esMultiploDe x y = mod x y == 0

sumarSoloMultiplos :: (Integer, Integer, Integer) -> Integer -> Bool -> Integer
sumarSoloMultiplos (a,b,c) d  | esMultiploDe a d || esMultiploDe b d || esMultiploDe cd == True = (a+b+c)
                              | otherwise = 0
                              
                              
                            
