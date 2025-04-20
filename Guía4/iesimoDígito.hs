cantDigitos :: Integer -> Integer
cantDigitos x | x == 0 = 0
              | x < 10 = 1
              | otherwise = cantDigitos (div x 10) + 1


iesimoDígito :: Integer -> Integer
iesimoDígito n i = mod ( div n 10^(cantDigitos (n)-i) 10)