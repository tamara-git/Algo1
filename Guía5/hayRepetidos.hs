{-hayRepetidos :: (Eq t) => [t] -> Bool seg´un la siguiente especificaci´on:
problema hayRepetidos (s: seq⟨T⟩) : B {
requiere: { True }
asegura: { resultado = true ↔ existen dos posiciones distintas de s con igual valor }
}-}

hayRepetidos :: (Eq t) => [t] -> Bool
hayRepetidos [] = False 
hayRepetidos (x:xs) | (x:xs) == [x] = False
                    | pertenece x xs = hayRepetidos (x:xs)
                    | otherwise = False