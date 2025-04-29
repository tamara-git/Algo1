{-hayRepetidos :: (Eq t) => [t] -> Bool seg´un la siguiente especificaci´on:
problema hayRepetidos (s: seq⟨T⟩) : B {
requiere: { True }
asegura: { resultado = true ↔ existen dos posiciones distintas de s con igual valor }
}-}

pertenece :: (Eq t) => t -> [t] -> Bool 
pertenece e [] = False
pertenece e (x:xs)  | e == x = True 
                    | otherwise = pertenece e (xs)

hayRepetidos :: (Eq t) => [t] -> Bool
hayRepetidos [] = False 
hayRepetidos (x:xs) | (x:xs) == [x] = False
                    | not (pertenece x xs) = False
                    | otherwise = hayRepetidos (xs)