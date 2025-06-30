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
minimoDivisor n desde | (desde > n) = 0
                      | (desde <= n) && (mod n desde == 0) = desde
                      | otherwise = minimoDivisor n (desde + 1)

esPrimo :: Int -> Bool
esPrimo n | minimoDivisor n 2 == n = True
          | otherwise = False 

primos :: Int -> Int -> [Int]
primos desde hasta | (desde > hasta) = []
               | (desde <= hasta) && (esPrimo desde == True) = desde:primos (desde+1) hasta 
               | otherwise = primos(desde+1) hasta


factoresPrimos :: Int -> [Int] -> [Int]
factoresPrimos n [] = []
factoresPrimos n (x:xs) | (mod n x == 0) = x:factoresPrimos (div n x) (x:xs)
                        | otherwise = factoresPrimos n xs

cantidadElementos :: [Int] -> Int
cantidadElementos [] = 0
cantidadElementos [x] = 1
cantidadElementos (x:xs) = 1 + cantidadElementos xs


esAtractivo :: Int -> Bool
esAtractivo n | esPrimo (cantidadElementos(factoresPrimos n (primos 2 n))) == True = True
              | otherwise = False


{--- EJERCICIO 3 (2 puntos)
-- problema palabraOrdenada (palabra: seq⟨Char⟩) : Bool {
--   requiere: {True}
--   asegura: {res = true <=> cada uno de los elementos no blancos de palabra es mayor o igual al anterior caracter no blanco, si existe alguno.}
-- }
-- Aclaración: 'a' < 'b' es True. -}

abecedario = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","k","y","z"]

indiceAbecedario :: [Char] -> Char -> Int
indiceAbecedario [] elemento = 0
indiceAbecedario (x:xs) elemento | elemento == x = 1
                                 | otherwise = 1 + indiceAbecedario xs elemento


esMenor :: [Char] -> Bool
esMenor (x:xs) | indiceAbecedario (x:xs) x < indiceAbecedario (x:xs) (head xs) = esMenor xs
               | otherwise = False 

palabraOrdenada :: [Char] -> Bool
palabraOrdenada [x] = True
palabraOrdenada (x:xs) | indiceAbecedario (x:xs) x < indiceAbecedario xs = True
                       | otherwise = Faldr