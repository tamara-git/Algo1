{-pares :: [Integer] -> [Integer] según la siguiente especificación:
problema pares (s: seq⟨Z⟩) : seq⟨Z⟩ {
requiere: { True }
asegura: {resultado sólo tiene los elementos pares de s en el orden dado, respetando las repeticiones}
}
-}
par :: Integer -> Integer
par x = 2*n

pares :: [Integer] -> [Integer]
pares (x:xs) | 
