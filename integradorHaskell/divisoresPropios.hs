{-Implementar la funci´on divisoresPropios :: Int ->[Int]
problema divisoresPropios (n: Z) : seq⟨Z⟩ {
requiere: {n > 0}
asegura: {res contiene a todos los divisores propios de n, ordenados de menor a mayor}
asegura: {res no tiene elementos repetidos}
asegura: {res no contiene a ning´un elemento que no sea un divisor propio de n}
}
-}

esDivisor :: Int -> Int -> Int
esDivisor n i | (i <= n) && (mod n i == 0) = i
              | otherwise = 0 

divisoresDeN :: Int -> Int -> [Int]
divisoresDeN n i | i > n = []
                 | otherwise = [esDivisor n i] ++ divisoresDeN n (i+1)

eliminarCeros :: [Int] -> [Int]
eliminarCeros [] = []
eliminarCeros [x] | x == 0 = []
eliminarCeros (x:xs) | x == 0 = eliminarCeros xs
                     | otherwise = x:eliminarCeros xs

divisoresPropios :: Int -> [Int]
divisoresPropios n = eliminarCeros(divisoresDeN n 1)

