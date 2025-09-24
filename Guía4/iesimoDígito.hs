{-problema cantDigitos (n: Z) : N {
requiere: { n ≥ 0 }
asegura: { n = 0 → resultado = 1}
asegura: { n ̸= 0 → (n div 10^resultado−1 > 0 ∧ n div 10^resultado = 0) }

-}
cantDigitosAux :: Integer -> Integer -> Integer
cantDigitosAux n i | n < 10^i = i 
                   | otherwise = 0 + cantDigitosAux n (i+1)

cantDigitos :: Integer -> Integer
cantDigitos n = cantDigitosAux n 1

{- problema iesimoDigito (n: Z, i: Z) : Z {
requiere: { n ≥ 0 ∧ (1 ≤ i ≤ cantDigitos(n)) }
asegura: { resultado = (n div 10^cantDigitos(n)−i
) mod 10 }
} -}

iesimoDigito :: Integer -> Integer -> Integer
iesimoDigito n i = mod (div n (10^(cantDigitos(n)-i))) 10 