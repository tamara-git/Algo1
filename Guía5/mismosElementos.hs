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
pertenece e (x:xs)  | e == x = True 
                    | otherwise = pertenece e (xs)

eliminarRepetidos :: (Eq t) => [t] -> [t]
eliminarRepetidos [] = []
eliminarRepetidos [x] = [x]
eliminarRepetidos (x:xs) | pertenece x xs == True = eliminarRepetidos (xs)
                         | otherwise = x:eliminarRepetidos(xs) 



mismosElementos :: (Eq t) => [t] -> [t] -> Bool
mismosElementos  [] []  = True
mismosElementos (x:xs) (y:ys) | pertenece y (eliminarRepetidos (x:xs)) && pertenece x (eliminarRepetidos (y:ys)) == True
                              | otherwise = False 