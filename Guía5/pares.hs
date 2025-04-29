{-pares :: [Integer] -> [Integer] según la siguiente especificación:
problema pares (s: seq⟨Z⟩) : seq⟨Z⟩ {
requiere: { True }
asegura: {resultado sólo tiene los elementos pares de s en el orden dado, respetando las repeticiones}
}
-}

pares :: [Integer] -> [Integer]
pares [x] = 
pares (x:xs) | x == esPar x = [x]
             | x /= esPar x = pares (xs)
             | otherwise = x:pares (xs) 
