{-Ejercicio 11. Implementar la funci´on losPrimerosNPerfectos :: Int ->[Int]
problema losPrimerosNPerfectos (n: Z) : seq⟨Z⟩ {
requiere: {n > 0}
asegura: {|res| = n}
asegura: {res es la lista de los primeros n n´umeros perfectos, de menor a mayor}
}
Por cuestiones de tiempos de ejecuci´on, no les recomendamos que prueben este ejercicio con un n > 4.-}


divisoresPropios :: Int -> [Int]
divisoresPropios n = divisoresDeN n 1 
    where 
        divisoresDeN :: Int -> Int -> [Int]
        divisoresDeN n i | i >= n = []
                         | mod n i == 0 = i:divisoresDeN n (i+1)
                         | otherwise = divisoresDeN n (i+1)

accederAElem :: [Int] -> Int -> Int
accederAElem [] i = 0 
accederAElem [x] 1 = x
accederAElem (x:xs) 1 = x
accederAElem (x:xs) i = accederAElem xs (i-1)

sumarElementos :: [Int] -> Int -> Int
sumarElementos [x] 1 = x
sumarElementos (x:xs) i = accederAElem (x:xs) i + sumarElementos xs i


nPerfectosDesde :: Int -> Int -> [Int]
nPerfectosDesde i n | i > n = []
nPerfectosDesde i n | (i <= n) && ((sumarElementos (divisoresPropios i) 1) == i) = [i] ++ nPerfectosDesde (i+1) n 
                    | otherwise = nPerfectosDesde (i+1) n


{-losPrimerosNPerfectos :: Int -> [Int]
losPrimerosNPerfectos 4 | sumarElementos (divisoresPropios n) == n = -}