{-Implementar la funci´on divisoresPropios :: Int ->[Int]
problema divisoresPropios (n: Z) : seq⟨Z⟩ {
requiere: {n > 0}
asegura: {res contiene a todos los divisores propios de n, ordenados de menor a mayor}
asegura: {res no tiene elementos repetidos}
asegura: {res no contiene a ning´un elemento que no sea un divisor propio de n}
}
-}

esDivisor :: Int -> Int -> Bool
esDivisor n i | mod n i == 0 = True
              | otherwise = False 

{-divisoresPropios :: Int -> [Int]
divisoresPropios n =-}
