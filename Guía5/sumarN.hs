{- sumarN :: Integer -> [Integer] -> [Integer] según la siguiente especificación:
problema sumarN (n: Z, s: seq⟨Z⟩) : seq⟨Z⟩ {
requiere: { True }
asegura: {|resultado| = |s| ∧ cada posición de resultado contiene el valor que hay en esa posición en s sumado
n }
}
-}

sumarN :: Integer -> [Integer] -> [Integer]
sumarN n [] = [n]
sumarN n [x] = [x + n]
sumarN n (x:xs) = [x + n] ++ sumarN n (xs)