{- eliminarRepetidos :: (Eq t) => [t] -> [t] que deja en la lista una única aparición de cada elemento, 
eliminando las repeticiones adicionales.-}

pertenece :: (Eq t) => t -> [t] -> Bool 
pertenece e [] = False
pertenece e (x:xs)  | e == x = True 
                    | otherwise = pertenece e (xs)

hayRepetidos :: (Eq t) => [t] -> Bool 
hayRepetidos (x:xs) | (x:xs) == [x] = True
                    | pertenece x xs == True = True
                    | otherwise = hayRepetidos (xs)

eliminarRepetidos :: (Eq t) => [t] -> [t]
eliminarRepetidos [x] = [x]
eliminarRepetidos (x:xs) | head xs == x = eliminarRepetidos (xs)
                         | otherwise = x:eliminarRepetidos(xs)