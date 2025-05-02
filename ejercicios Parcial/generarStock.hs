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

--generarStock me devuelve la recursión de listas de palabras 
generarStock :: [String] -> [(String, Int)]
generarStock [x]= [(x,1)]
generarStock (x:xs) = [(x,cantidadApariciones x (x:xs))] ++ generarStock xs