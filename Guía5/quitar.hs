{-quitar :: (Eq t) => t -> [t] -> [t], que dados un entero x y una lista xs, elimina la primera 
aparición de x en la lista xs (de haberla).-}

quitar :: (Eq t) => t -> [t] -> [t]
quitar x [] = []
quitar x (xs) | xs == [x] = []
              | head (xs) /= x = (xs)
              | otherwise = quitar x (tail xs) 
{-problema quitarTodos -}

quitarTodos :: (Eq t) => t -> [t] -> [t]
quitarTodos x xs | head (xs) == x = quitarTodos x (tail xs)
                 | otherwise = head [xs] ++ quitarTodos x (tail xs)