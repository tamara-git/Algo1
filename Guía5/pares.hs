{-pares :: [Integer] -> [Integer] según la siguiente especificación:
problema pares (s: seq⟨Z⟩) : seq⟨Z⟩ {
requiere: { True }
asegura: {resultado sólo tiene los elementos pares de s en el orden dado, respetando las repeticiones}
}
-}

esPar :: Integer -> Integer
esPar x = mod x 2 == 0

pares :: [Integer] -> [Integer]
pares (x:xs) | x == esPar x = [x]
             | x /= esPar x = pares (xs)
             | otherwise = x:pares (xs) 
