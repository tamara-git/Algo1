{- eliminarRepetidos :: (Eq t) => [t] -> [t] que deja en la lista una única aparición de cada elemento, 
eliminando las repeticiones adicionales.-}
hayRepetidos :: (Eq t) => [t] -> Bool
hayRepetidos [] = False 
hayRepetidos (x:xs) | (x:xs) == [x] = False
                    | head xs == x = hayRepetidos (xs)
                    | otherwise = False 
                                        
eliminarRepetidos :: (Eq t) => [t] -> [t]
eliminarRepetidos [x] = [x]
eliminarRepetidos (x:xs) | x /= head xs = eliminarRepetidos (xs)
                         | otherwise = x:eliminarRepetidos(xs)