{- eliminarRepetidos :: (Eq t) => [t] -> [t] que deja en la lista una única aparición de cada elemento, 
eliminando las repeticiones adicionales.-}

pertenece :: (Eq t) => t -> [t] -> Bool 
pertenece e [] = False
pertenece e (x:xs)  | e == x = True 
                    | otherwise = pertenece e (xs)

eliminarRepetidos :: (Eq t) => [t] -> [t]
eliminarRepetidos [] = []
eliminarRepetidos [_] = [_]
eliminarRepetidos (x:xs) =  pertenece x xs == True =  eliminarRepetidos (xs)
                         
