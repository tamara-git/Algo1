{- sumarElUltimo :: [Integer] -> [Integer] seg´un la siguiente especificaci´on:
problema sumarElUltimo (s: seq⟨Z⟩) : seq⟨Z⟩ {
requiere: { |s| > 0 }
asegura: {resultado = sumarN(s[|s| − 1], s) }
}
Por ejemplo sumarElUltimo [1,2,3] da [4,5,6]
-}

ultimo :: [t] -> t 
ultimo [x] = x
ultimo (_:xs) = ultimo (xs)

sumarN :: Integer -> [Integer] -> [Integer]
sumarN n [] = [n]
sumarN n [x] = [x + n]
sumarN n (x:xs) = [x + n] ++ sumarN n (xs)

sumarElUltimo :: [Integer] -> [Integer]
sumarElUltimo [x] = [x+x]
sumarElUltimo (x:xs) = sumarN (ultimo (x:xs)) (x:xs)