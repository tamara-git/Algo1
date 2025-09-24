{-quitar :: (Eq t) => t -> [t] -> [t], que dados un entero x y una lista xs, elimina la primera aparici´on de x en
la lista xs de haberla-}

quitar :: (Eq t) => t -> [t] -> [t]
quitar x (y:ys) | x == y = x:quitar x ys
                | otherwise = quitar x ys