{-pares :: [Integer] -> [Integer] según la siguiente especificación:
problema pares (s: seq⟨Z⟩) : seq⟨Z⟩ {
requiere: { True }
asegura: {resultado sólo tiene los elementos pares de s en el orden dado, respetando las repeticiones}
}
-}

pares :: [Integer] -> [Integer]
pares [] = []
pares (x:xs) | (mod x 2 == 0) = x:pares (xs)
             | otherwise = pares (xs)