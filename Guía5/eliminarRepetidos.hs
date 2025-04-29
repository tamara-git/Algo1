{- eliminarRepetidos :: (Eq t) => [t] -> [t] que deja en la lista una única aparición de cada elemento, 
eliminando las repeticiones adicionales.-}

hayRepetidos :: (Eq t) => [t] -> Bool 
hayRepetidos (x:xs) | (x:xs) == [x] = True
                    | pertenece x xs == True = True
                    | otherwise = hayRepetidos (xs)

eliminarRepetidos :: (Eq t) => [t] -> [t]
eliminarRepetidos [x] = [x]
eliminarRepetidos (x:xs) | hayRepetidos (x:xs) == False = (x:xs)
                         | otherwise = x:(eliminarRepetidos(xs)) 