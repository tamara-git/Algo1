{-1. sumatoria :: [Integer] -> Integer según la siguiente especificación:
problema sumatoria (s: seq⟨Z⟩) : Z {
requiere: { True }
asegura: { resultado = sumatoria desde i= 0 hasta |s| - 1 de s[i]}
}
-}

sumatoria :: [Integer] -> Integer
sumatoria [] = 0
sumatoria [x] = x 
sumatoria (x:xs) = x + sumatoria xs  

{-2. productoria :: [Integer] -> Integer según la siguiente especificación:
problema productoria (s: seq⟨Z⟩) : Z {
requiere: { True }
asegura: { resultado = Productoria desde i = 0 hasta |s|−1 de s[i] }
}-}

productoria :: [Integer] -> Integer
productoria [] = 0 
productoria [x] = x
productoria (x:xs) = x * productoria xs

{-3.maximo :: [Integer] -> Integer según la siguiente especificación:
problema maximo (s: seq⟨Z⟩) : Z {
requiere: {|s| > 0}
asegura: {resultado ∈ s ∧ todo elemento de s es menor o igual a resultado}
}-}

maximo :: [Integer] -> Integer
maximo [x] = x
maximo (x:xs) | x >= maximo xs = x 
              | otherwise = maximo xs



{-4. sumarN :: Integer -> [Integer] -> [Integer] según la siguiente especificación:
problema sumarN (n: Z, s: seq⟨Z⟩) : seq⟨Z⟩ {
requiere: { True }
asegura: {|resultado| = |s| ∧ cada posición de resultado contiene el valor que hay en esa posici´on en s sumado
n }
}-}

sumarN :: Integer -> [Integer] -> [Integer]
sumarN n [] = []
sumarN n [x] = [x + n]
sumarN n (x:xs) = [x+n] ++ sumarN n xs

{-5. sumarElPrimero :: [Integer] -> [Integer] según la siguiente especificación:
problema sumarElPrimero (s: seq⟨Z⟩) : seq⟨Z⟩ {
requiere: { |s| > 0 }
asegura: {resultado = sumarN (s[0], s) }
}-}

sumarElPrimero :: [Integer] -> [Integer] 
sumarElPrimero [x] = [x + x]
sumarElPrimero (x:xs) = sumarN x (x:xs)

{-6. sumarElUltimo :: [Integer] -> [Integer] según la siguiente especificación:
problema sumarElUltimo (s: seq⟨Z⟩) : seq⟨Z⟩ {
requiere: { |s| > 0 }
asegura: {resultado = sumarN (s[|s| − 1], s) }
}
Por ejemplo sumarElUltimo [1,2,3] da [4,5,6]-}

ultimo :: [Integer] -> Integer
ultimo [x] = x 
ultimo (x:xs) = ultimo xs

sumarElUltimo :: [Integer] -> [Integer]
sumarElUltimo [x] = [x+x]
sumarElUltimo (x:xs) = sumarN (ultimo (x:xs)) (x:xs)

{-7. pares :: [Integer] -> [Integer] seg´un la siguiente especificaci´on:
problema pares (s: seq⟨Z⟩) : seq⟨Z⟩ {
requiere: { True }
asegura: {resultado s´olo tiene los elementos pares de s en el orden dado, respetando las repeticiones}
}
Por ejemplo pares [1,2,3,5,8,2] da [2,8,2]-}

pares :: [Integer] -> [Integer]
pares [] = []
pares [x] | mod x 2 == 0 = [x]
          | otherwise = []
pares (x:xs) | mod x 2 == 0 = x:pares xs
             | otherwise = pares xs

{-8. multiplosDeN :: Integer -> [Integer] -> [Integer] que dado un n´umero n y una lista xs, devuelve una lista
con los elementos de xs m´ultiplos de n.-}

multiplosDeN :: Integer -> [Integer] -> [Integer] 
multiplosDeN n [] = []
multiplosDeN n [x] | mod x n == 0 = [x]
                   | otherwise = []
multiplosDeN n xs | mod (head xs) n == 0 = (head xs):multiplosDeN n (tail xs)
                  | otherwise = multiplosDeN n (tail xs)

{-9. ordenar :: [Integer] -> [Integer] que ordena los elementos de la lista en forma creciente. Sugerencia: Pensar
c´omo pueden usar la funci´on m´aximo para que ayude a generar la lista ordenada necesaria-}

{- ordenar :: [Integer] -> [Integer] que ordena los elementos de la lista en forma creciente. Sugerencia: Pensar
cómo pueden usar la función maximo para que ayude a generar la lista ordenada necesaria.
-}

quitar :: Integer -> [Integer] -> [Integer]
quitar x [] = []
quitar x [y] | x == y = []
             | otherwise = [y]
quitar x (y:ys) | x == y = ys 
                | otherwise = y:quitar x ys

ordenar :: [Integer] -> [Integer]
ordenar [] = []
ordenar [x] = [x]
ordenar (x:xs) = ordenar (quitar (maximo(x:xs)) (x:xs)) ++ [maximo (x:xs)]

--Hecho con mínimo
minimo :: [Integer] -> Integer
minimo [] = 0
minimo [x] = x
minimo (x:xs) | x <= minimo xs = x
              | otherwise = minimo (xs)  

ordenar2 :: [Integer] -> [Integer]
ordenar2 [] = []
ordenar2 [x] = [x]
ordenar2 xs = minimo (xs) : ordenar2 (quitar (minimo xs) xs)
