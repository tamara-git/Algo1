--["madera", "clavo", "pala", "clavo"]
--[("madera", 1),("clavo",2),("pala",1)]

--generarStock :: [String] -> [(String, Int)]

pertenece :: String -> [String] -> Bool
pertenece _ [] = False
pertenece palabra (x : xs) = palabra == x || pertenece palabra xs

quitar :: String -> [String] -> [String]
quitar palabra (_:[]) = []
quitar palabra (x:xs) | palabra == x = quitar palabra xs
                        | otherwise = x: quitar palabra xs

filtrarRepetidos :: [String] -> [String]
filtrarRepetidos (x:[]) = [x] 
filtrarRepetidos (x:xs) | pertenece x xs == True = x: quitar x xs 
                        | otherwise = x: filtrarRepetidos xs   

cantidadApariciones :: String -> [String] -> Int
cantidadApariciones y [] = 0
cantidadApariciones y (x:xs) | y == x = 1 + cantidadApariciones y (xs)
                             | otherwise = cantidadApariciones y (xs)

{-crearTupla :: (String, [String]) -> (String, Int)
crearTupla (palabra,(x:xs)) = (palabra, cantidadApariciones palabra (x:xs))

quitalo :: [(String, Int)] -> [String]
quitalo [(palabra,1)] = []
quitalo [(palabra,n)] = [] 
-}

--generarStock me devuelve la recursión de listas de palabras 
generarStockAux :: [String] -> [String] -> [(String, Int)]
generarStockAux [] _ = []
generarStockAux (x:xs) yaContadas | pertenece x yaContadas = generarStockAux xs yaContadas
                                  | otherwise = [(x,cantidadApariciones x (x:xs))]: generarStockAux xs yaContadas

generarStock :: [String] -> [(String, Int)]
generarStock [x] = [(x,1)]
generarStock (x:xs) = generarStockAux (x:xs) []


{-
igualesContiguos :: [String] -> [String]
igualesContiguos (x:y:xs) | x == y = y:(x:xs)
                          | otherwise = igualesContiguos x:(y:xs)  

--agarrame el de mayor cantidad
elMasGrande :: [String] -> [(String, Int)] -> [(String, Int)] 
elMasGrande | (cantidadApariciones x (x:xs) > cantidadApariciones head xs (x:xs)) = quitalo [(head xs, cantidadApariciones head xs (x:xs))]
                   | otherwise =  
-}