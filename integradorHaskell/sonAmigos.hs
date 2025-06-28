{-Ejercicio 10. Implementar la funci´on sonAmigos :: Int ->Int ->Bool
problema sonAmigos (n,m: Z) : Bool {
requiere: {n > 0}
requiere: {m > 0}
requiere: {m ̸= n}
asegura: {res = True ⇔ n y m son n´umeros amigos}
}
-}


divisoresPropios :: Int -> [Int]
divisoresPropios n = divisoresdeN n 1
    where
        divisoresdeN :: Int -> Int -> [Int]
        divisoresdeN n i | i >= n = []
                         | (i < n) && (mod n i == 0) = i:divisoresdeN n (i+1)
                         | otherwise = divisoresdeN n (i+1) 

accederAElem :: [Int] -> Int -> Int
accederAElem [] i = 0
accederAElem [x] 1 = x
accederAElem (x:xs) 1 = x
accederAElem (x:xs) i = accederAElem xs (i-1)

sumarDivisores :: [Int] -> Int -> Int
sumarDivisores [] i = 0
sumarDivisores [x] 1 = x
sumarDivisores (x:xs) i = accederAElem (x:xs) i + sumarDivisores xs i

sonAmigos :: Int -> Int -> Bool
sonAmigos n m | (n == (sumarDivisores (divisoresPropios m) 1)) && (m == (sumarDivisores (divisoresPropios m) 1)) = True
              | otherwise = False