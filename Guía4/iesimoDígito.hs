{- problema iesimoDigito (n: Z, i: Z) : Z {
requiere: { n ≥ 0 ∧ 1 ≤ i ≤ cantDigitos(n) }
asegura: { resultado = (n div 10cantDigitos(n)−i
) mod 10 }
}

problema cantDigitos (n: Z) : N {
requiere: { n ≥ 0 }
asegura: { n = 0 → resultado = 1}
asegura: { n ̸= 0 → (n div 10^resultado−1 > 0 ∧ n div 10^resultado = 0) }
-}

cantDigitos :: Integer -> Integer
cantDigitos x | x == 0 = 0
              | x < 10 = 1
              | otherwise = cantDigitos (div x 10) + 1

iesimoDígito :: Integer -> Integer
iesimoDígito n i = mod (div n 10^(cantDigitos (n)-i) 10)