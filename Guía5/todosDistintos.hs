{-todosDistintos :: (Eq t) => [t] -> Bool según la siguiente especificación:
problema todosDistintos (s: seq⟨T⟩) : B {
requiere: { True }
asegura: { resultado = false ↔ existen dos posiciones distintas de s con igual valor }
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