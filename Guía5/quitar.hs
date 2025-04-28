{-quitar :: (Eq t) => t -> [t] -> [t], que dados un entero x y una lista xs, elimina la primera 
aparición de x en la lista xs (de haberla).-}

quitar :: (Eq t) => t -> [t] -> [t]
quitar x [] = []
quitar x (xs) | (xs) == [x] = []
              | head xs == x = tail xs
              | otherwise = (head xs : quitar x (tail xs))

{- quitarTodos :: (Eq t ) => t -> [t] -> [t], que dados un entero x y una lista xs, elimina todas las apariciones
de x en la lista xs (de haberlas). Es decir:
problema quitarTodos (e: T, s: seq⟨T⟩) : seq⟨T⟩ {
requiere: { True }
asegura: { resultado es igual a s pero sin el elemento e. }
}-}

quitarTodos :: (Eq t ) => t -> [t] -> [t]
quitarTodos x [] = []
quitarTodos x (y:xs) | (y:xs) == [x] = []
                     | y == x = xs
                     | otherwise = (y:quitarTodos x (tail xs))
