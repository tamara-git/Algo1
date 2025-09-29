{-1. sumatoria :: [Integer] -> Integer según la siguiente especificación:
problema sumatoria (s: seq⟨Z⟩) : Z {
requiere: { True }
asegura: { resultado = sumatoria desde i= 0 hasta |s| - 1 de s[i]}
}
-}

sumatoria :: [Integer] -> Integer
sumatoria [] = 0
sumatoria [x] = x 
sumatoria (x:xs) = x + sumatoria xs  

{-2. productoria :: [Integer] -> Integer según la siguiente especificación:
problema productoria (s: seq⟨Z⟩) : Z {
requiere: { True }
asegura: { resultado = Productoria desde i = 0 hasta |s|−1 de s[i] }
}-}

productoria :: [Integer] -> Integer
productoria [] = 0 
productoria [x] = x
productoria (x:xs) = x * productoria xs

{-3.maximo :: [Integer] -> Integer según la siguiente especificación:
problema maximo (s: seq⟨Z⟩) : Z {
requiere: {|s| > 0}
asegura: {resultado ∈ s ∧ todo elemento de s es menor o igual a resultado}
}-}

maximo :: [Integer] -> Integer
maximo [x] = x
maximo (x:xs) | x >= maximo xs = x 
              | otherwise = maximo xs



{-4. sumarN :: Integer -> [Integer] -> [Integer] según la siguiente especificación:
problema sumarN (n: Z, s: seq⟨Z⟩) : seq⟨Z⟩ {
requiere: { True }
asegura: {|resultado| = |s| ∧ cada posición de resultado contiene el valor que hay en esa posici´on en s sumado
n }
}-}

sumarN :: Integer -> [Integer] -> [Integer]
sumarN n [] = []
sumarN n [x] = [x + n]
sumarN n (x:xs) = [x+n] ++ sumarN n xs