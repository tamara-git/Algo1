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
        divisoresDeN n i | mod n i == 0 = i:divisoresDeN n (i+1)
                         | otherwise = divisoresDeN n (i+1)

accederAElem :: [Int] -> Int -> Int
accederAElem [] i = 0
accederAElem [x] 1 = x
accederAElem (x:xs) 1 = x
accederAElem (x:xs) i = accederAElem xs (i-1)

sumarElementos :: [Int] -> Int -> Int
sumarElementos [x] i = x
sumarElementos (x:xs) i n = | i <= n = accederAElem (x:xs) i + sumarElementos (x:xs) (i+1)

{-losPrimerosNPerfectos :: Int -> [Int]
losPrimerosNPerfectos n | -}