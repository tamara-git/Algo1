{-todosDistintos :: (Eq t) => [t] -> Bool según la siguiente especificación:
problema todosDistintos (s: seq⟨T⟩) : B {
requiere: { True }
asegura: { resultado = false ↔ existen dos posiciones distintas de s con igual valor }
}-}

todosIguales :: (Eq t) => [t] -> Bool
todosIguales [] = True
todosIguales (x:xs) | (x:xs) == [x] = True
                    | head xs == x = todosIguales (xs)
                    | otherwise = False 

todosDistintos :: (Eq t) => [t] -> Bool
todosDistintos [] = True
todosDistintos (x:xs) | (x:xs) == [x] = True
                      | todosIguales (x:xs) == True = False
                      | otherwise = x:todosDistintos (xs)