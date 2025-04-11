{-Dada una terna de números enteros y un natural, calcula la suma de los elementos de la terna que son 
múltiplos del número natural.-}
sumarSoloMultiplos :: (Integer, Integer, Integer) -> Integer -> Integer
sumarSoloMultiplos (a,b,c) d  | (mod a d == 0)  && (mod b d == 0)  && (mod c d == 0) = (a+b+c)
                              | otherwise = 0