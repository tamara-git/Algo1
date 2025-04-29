{-todosDistintos :: (Eq t) => [t] -> Bool según la siguiente especificación:
problema todosDistintos (s: seq⟨T⟩) : B {
requiere: { True }
asegura: { resultado = false ↔ existen dos posiciones distintas de s con igual valor }
}-}

todosDistintos :: (Eq t) => [t] -> Bool
todosDistintos [] = True
todosDistintos (x:xs) | (x:xs) == [x] = True
                      | head xs == x = todosDistintos (xs)
                      | otherwise = x:(todosDistintos (xs)) == True 