{-maximo :: [Integer] -> Integer seg´un la siguiente especificaci´on:
problema maximo (s: seq⟨Z⟩) : Z {
requiere: { |s| > 0 }
asegura: { resultado ∈ s ∧ todo elemento de s es menor o igual a resultado }
}-}

maximo :: [Integer] -> Integer 
maximo [x] = x
maximo (x:xs) | x >= maximo xs = x 
              | otherwise = maximo xs
