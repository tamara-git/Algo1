{-   1. pertenece :: (Eq t) => t -> [t] -> Bool según la siguiente especificación:
problema pertenece (e: T, s: seq⟨T⟩) : B {
requiere: { True }
asegura: { resultado = true ↔ e ∈ s }
}-}

pertenece :: (Eq t) => t -> [t] -> Bool 
pertenece e (x:xs) | (x:xs) == [] = False
                   | (x:xs) == [e] = True
                   | pertenece 