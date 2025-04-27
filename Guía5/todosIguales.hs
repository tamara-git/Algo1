{-todosIguales :: (Eq t) => [t] -> Bool, 
que dada una lista devuelve verdadero sí y solamente sí todos sus elementos son iguales.
-}

todosIguales :: (Eq t) => [t] -> Bool
todosIguales [] = True
todosIguales [x] = True
todosIguales (x:xs) | (x:xs) == [x] = True
                    | otherwise = x == todosIguales (xs) 

