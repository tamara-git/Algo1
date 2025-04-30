{-productoria :: [Integer] -> Integer según la siguiente especificación:
problema productoria (s: seq⟨Z⟩) : Z {
requiere: { T rue }
asegura: { resultado = productoria desde i=0 hasta |s|−1 de s[i] }
}
-}

productoria :: [Integer] -> Integer
productoria [] = 0
productoria [x] = x 
productoria (x:xs) = x * productoria (xs)