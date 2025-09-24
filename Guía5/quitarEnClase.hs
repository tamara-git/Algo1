{-quitar :: (Eq t) => t -> [t] -> [t], que dados un entero x y una lista xs, elimina la primera aparici´on de x en
la lista xs de haberla-}

quitar :: (Eq t) => t -> [t] -> [t]
quitar x [] = []
quitar x [y] | x == y = []
             | otherwise = [y]
quitar x (y:ys) | x == y = ys 
                | otherwise = y:quitar x ys


{-quitarTodos :: (Eq t ) => t -> [t] -> [t], que dados un entero x y una lista xs, elimina todas las apariciones
de x en la lista xs (de haberlas). Es decir:
problema quitarTodos (e: T , s: seq⟨T ⟩) : seq⟨T ⟩ {
requiere: { T rue }
asegura: { resultado es igual a s pero sin el elemento e. }
}-}

quitarTodos :: (Eq t ) => t -> [t] -> [t]
quitarTodos x [] = []
quitarTodos x [y] | x == y = []
                  | otherwise = [y]
quitarTodos x (y:ys) | x == y = quitarTodos x ys
                     | otherwise = y:quitarTodos x ys