{- sumarElPrimero :: [Integer] -> [Integer] según la siguiente especificación:
problema sumarElPrimero (s: seq⟨Z⟩) : seq⟨Z⟩ {
requiere: { |s| > 0 }
asegura: {resultado = sumarN(s[0], s) }
}
Por ejemplo sumarElPrimero [1,2,3] da [2,3,4]-}

sumarN :: Integer -> [Integer] -> [Integer]
sumarN n [] = [n]
sumarN n [x] = [x + n]
sumarN n (x:xs) = [x + n] ++ sumarN n (xs)

sumarElPrimero :: [Integer] -> [Integer]
sumarElPrimero [x] = [x+1]
sumarElPrimero (x:xs) = sumarN 1 (x:xs)