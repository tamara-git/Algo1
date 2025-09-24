{-hayRepetidos :: (Eq t) => [t] -> Bool seg´un la siguiente especificaci´on:
problema hayRepetidos (s: seq⟨T⟩) : B {
requiere: { True }
asegura: { resultado = true ↔ existen dos posiciones distintas de s con igual valor }
}-}

pertenece :: (Eq t) => t -> [t] -> Bool 
pertenece e [] = False
pertenece e (x:xs)  | e == x = True 
                    | otherwise = pertenece e (xs)

todosDistintos :: (Eq t) => [t] -> Bool
todosDistintos [] = True
todosDistintos (x:xs) | (x:xs) == [x] = True
                      |  pertenece x xs == True = False
                      | otherwise = todosDistintos (xs)

hayRepetidos :: (Eq t) => [t] -> Bool 
hayRepetidos (x:xs) | (x:xs) == [x] = False
                    | pertenece x xs == True = True
                    | otherwise = hayRepetidos (xs)

-- Otra forma pero sin recursión directa en hayRepetidos
{- hayRepetidos xs = not (todosDistintos xs) -}