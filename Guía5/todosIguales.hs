{-todosIguales :: (Eq t) => [t] -> Bool, 
que dada una lista devuelve verdadero sí y solamente sí todos sus elementos son iguales.
-}

todosIguales :: (Eq t) => [t] -> Bool
todosIguales [] = True
todosIguales (x:xs) | [x] == x = True
                    |otherwise = [x] == todosIguales (xs) 

