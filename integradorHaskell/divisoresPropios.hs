{-Implementar la funci´on divisoresPropios :: Int ->[Int]
problema divisoresPropios (n: Z) : seq⟨Z⟩ {
requiere: {n > 0}
asegura: {res contiene a todos los divisores propios de n, ordenados de menor a mayor}
asegura: {res no tiene elementos repetidos}
asegura: {res no contiene a ning´un elemento que no sea un divisor propio de n}
}
-}

divisordeN :: Int -> Int -> [Int]
divisordeN i n | (i <= n) and (mod n i == 0) = [i] ++ divisordeN (i+1) n
               | otherwise = divisordeN (i+1) n 

{-divisoresPropios :: Int -> [Int]
divisoresPropios-}