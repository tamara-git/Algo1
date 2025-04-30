{-sumatoria :: [Integer] -> Integer según la siguiente especificación:
problema sumatoria (s: seq⟨Z⟩) : Z {
requiere: { True }
asegura: { resultado = sumatoria desde i=0 hasta |s|−1  s[i] }
}
-}

principio :: [t] -> [t]
principio [x] = []
principio (x:xs) = x:principio  xs 

sumatoria :: [Integer] -> Integer
sumatoria [] = 0
sumatoria [x] = x
sumatoria (x:xs) = sumatoria (principio (x:xs)) 
