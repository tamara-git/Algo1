--["madera", "clavo", "pala", "clavo"]
--[("madera", 1),("clavo",2),("pala",1)]

--generarStock :: [String] -> [(String, Int)]

pertenece :: String -> [String] -> Bool
pertenece _ [] = False
pertenece palabra (pal : xs) = palabra == pal || pertenece palabra xs

quitar :: String -> [String] -> [String]
quitar palabra (_:[]) = []
quitar palabra (pal:xs) | palabra == pal = quitar palabra xs
                        | otherwise = pal: quitar palabra xs

filtrarRepetidos :: [String] -> [String]
filtrarRepetidos (x:[]) = [x] 
filtrarRepetidos (pal:xs) | pertenece pal xs == True = pal: quitar pal xs
                          | otherwise = pal: filtrarRepetidos xs
                        
cantidadApariciones :: String -> [String] -> Int
cantidadApariciones y [] = 0
cantidadApariciones y (x:xs) | y == x = 1 + cantidadApariciones y (xs)
                             | otherwise = cantidadApariciones y (xs)

--generarStock me devuelve la recursión de listas de palabras 
generarStock :: [String] -> [(String, Int)]
generarStock [x]= [(x,1)]
generarStock (y:xs) = [(y,cantidadApariciones y (y:xs))] ++ generarStock xs