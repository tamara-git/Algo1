{-mismosElementos :: (Eq t) => [t] -> [t] -> Bool, que dadas dos listas devuelve 
verdadero sí y solamente sí ambas listas contienen los mismos elementos, 
sin tener en cuenta repeticiones, es decir:
problema mismosElementos (s: seq⟨T⟩, r: seq⟨T⟩) : B {
requiere: { True }
asegura: { resultado = true ↔ todo elemento de s pertenece r y viceversa }
}
-}
 
pertenece :: (Eq t) => t -> [t] -> Bool 
pertenece e [] = False
pertenece e (x:xs) = e == x || pertenece e (xs)

quitarTodos :: (Eq t) => t -> [t] -> [t]
quitarTodos x [] = []
quitarTodos x (y:xs) | (y:xs) == [x] = []
                     | y == x = quitarTodos x (xs) 
                     | otherwise = y:quitarTodos x (xs)

mismosElementos :: (Eq t) => [t] -> [t] -> Bool
mismosElementos  [] []  = True
mismosElementos (x:xs) (y:ys) | not (pertenece x (y:ys)) = False
                              | otherwise = mismosElementos (quitarTodos x (x:xs)) (quitarTodos x (y:ys)) 