-- EJERCICIO 1 (2 puntos)
-- problema mediaMovilN (lista: seq⟨Z⟩, n: Z) : Float {
--   requiere: {|lista| > 0}
--   requiere: {n > 0 ∧ n ≤ |lista|}
--   asegura: {res es el promedio de los últimos n elementos de lista}
-- }

len :: [Int] -> Int
len [x] = 1
len (x:xs) = 1 + len xs 

elementoEnIndice :: [Int] -> Int -> Int
elementoEnIndice [] i = 0
elementoEnIndice [x] 1 = x
elementoEnIndice (x:xs) 1 = x 
elementoEnIndice (x:xs) i = elementoEnIndice xs (i-1)


listaDesdeN :: [Int] -> Int -> Int -> [Int]
listaDesdeN [x] 1 1 = [x]
listaDesdeN (x:xs) desde hasta | (desde <= hasta) && (hasta <= len (x:xs)) = (elementoEnIndice (x:xs) desde): listaDesdeN (x:xs) (desde + 1) hasta
                               | otherwise = []

sumarElementos :: [Int] -> Int
sumarElementos [x] = x
sumarElementos (x:xs) = x + sumarElementos xs

promedio :: [Int] -> Float
promedio [x] = fromIntegral x / fromIntegral (len [x])
promedio (x:xs) = fromIntegral (sumarElementos (x:xs)) / fromIntegral (len (x:xs))  


mediaMovilN :: [Int] -> Int -> Float 
mediaMovilN [x] 1 = fromIntegral x 
mediaMovilN (x:xs) n = promedio (listaDesdeN (x:xs) n (len (x:xs)))

{--- EJERCICIO 2 (2 puntos)    n>0
-- problema esAtractivo (n: Z) : Bool {
--   requiere: {n > 0}
--   asegura: {res = true <=> la cantidad de factores primos de n (distintos o no) es también un número primo.}
-- }
-- Aclaración: los factores primos de 30 son [5,3,2]. Los factores primos de 9 son [3,3]. -}

minimoDivisor :: Int -> Int -> Int
minimoDivisor n desde | (mod n desde == 0) = desde
                      | otherwise = minimoDivisor n (desde + 1)

esPrimo :: Int -> Bool
esPrimo n | minimoDivisor n 2 == n = True
          | otherwise = False 

esAtractivo :: Int -> Bool
esAtractivo n | 