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

--crearTupla :: (String, [String]) -> (String, Int)
--crearTupla (palabra,(x:xs)) = (palabra, cantidadApariciones palabra (x:xs))

--generarStockAux :: [String] -> [String] -> [(String, Int)]
--generarStockAux [x] = [(x,1)]
--generarStockAux (filtrarRepetidos (x:xs)) (x:xs) = crearTupla (x, cantidadApariciones x ())

quitalo :: [(String, Int)] -> [(String, Int)]
quitalo [(palabra,1)] = []
quitalo [(palabra, cantidadApariciones palabra (x:xs))] = []

--generarStock me devuelve la recursión de listas de palabras 
generarStockAux :: [String] -> [(String, Int)]
generarStockAux [x]= [(x,1)]
generarStockAux (x:xs) = [(x,cantidadApariciones x (x:xs))] ++ generarStockAux xs

--agarrame el más grande
--elMasGrande :: [(String, Int)] -> [(String, Int)] 
--elMasGrande (x:xs) | (head xs == x) && (cantidadApariciones x (x:xs) > cantidadApariciones head xs (x:xs)) = quitarlo
                  -- | otherwise =  
