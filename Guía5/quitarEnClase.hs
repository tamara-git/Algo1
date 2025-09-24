{-quitar :: (Eq t) => t -> [t] -> [t], que dados un entero x y una lista xs, elimina la primera aparici´on de x en
la lista xs de haberla-}

quitar :: (Eq t) => t -> [t] -> [t]
quitar x [] = []
quitar x [y] | x == y = []
             | otherwise = [y]
quitar x (y:ys) | x == y = ys 
                | otherwise = y:quitar x ys