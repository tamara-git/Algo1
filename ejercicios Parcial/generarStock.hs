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
-}

--generarStock me devuelve la recursión de listas de palabras 
--generarStockAux :: [String] -> [String] -> [(String, Int)]
--generarStockAux (x:xs) filtrados | pertece x filtrados = generarStock (xs) filtrados
--                                 | otherwise = (x, 1 + cantidadApariciones x (xs)): generarStock (xs) filtrados 
--where filtrados = filtrarRepetidos (x:xs)

--generarStock :: [String] -> [(String, Int)]
--generarStock (x:[]) = [(x,1)] 
--generarStock (x:xs) | [(x,cantidadApariciones x (x:xs))] ++ generarStock (xs)

--agarrame el de mayor cantidad

elMasGrande :: String -> [String] -> [(String, Int)] 
elMasGrande palabra [] = []
elMasGrande palabra (x:xs) | cantidadApariciones palabra (x:xs) > cantidadApariciones palabra (xs) = [(palabra,cantidadApariciones palabra (x:xs))]  
                           | otherwise = [(palabra,cantidadApariciones palabra (xs))] 

recursiónMasGrande :: [String] -> [(String,Int)]
recursionMasGrande [x] = [x,1]
recursiónMasGrande (x:xs) = elMasGrande x (x:xs) ++ elMasGrande head xs (x:xs) ++ recursionMasGrande (tail xs)