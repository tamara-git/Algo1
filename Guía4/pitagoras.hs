{-Especificar e implementar una función pitagoras :: Integer ->Integer ->Integer ->Integer que dados
m, n , r ∈ N≥0, cuente cuántos pares (p, q) con 0 ≤ p ≤ m y 0 ≤ q ≤ n satisfacen que p^2 + q^2 ≤ r^2
. Por ejemplo:
pitagoras 3 4 5 ⇝ 20
pitagoras 3 4 2 ⇝ 6 -}

pitagorasQVariable :: Integer -> Integer -> Integer -> Integer -> Integer -> Integer
pitagorasQVariable m n r p q  
                             | (p <= m) && (q <= n) && (p^2 + q^2 <= r^2) = 1 + pitagorasQVariable m n r p (q+1)
                             | (p <= m) && (q <= n) && (p^2 + q^2 > r^2) = 0 + pitagorasQVariable m n r p (q+1)
                             | otherwise = 0 

pitagorasPyQVariables  :: Integer -> Integer -> Integer -> Integer -> Integer
pitagorasPyQVariables m n r p | p <= m = pitagorasQVariable m n r p 0 + pitagorasPyQVariables m n r (p+1) 
                              | otherwise = 0
                              
pitagoras :: Integer -> Integer -> Integer -> Integer
pitagoras m n r = pitagorasPyQVariables m n r 0
--pitagoras m n r = pitagorasPVariable m n r 0 0 + pitagorasQVariable m n r 1 0