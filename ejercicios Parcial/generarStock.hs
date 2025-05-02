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
                        
cantidadRepeticiones :: String -> [String] -> Int
cantidadRepeticiones (x:[]) = 0
cantidadRepeticiones pal (pal:xs) | pal == head xs = 1 + cantidadRepeticiones pal (tail xs)
                                  | otherwise = cantidadRepeticiones pal (tail xs)

--generarStock me devuelve la recursión de listas de palabras 
{-generarStock :: [String] -> [(String, Int)]
generarStock (x:[]) = [x,0]
generarStock (pal:xs) | [(pal,cantidadRepeticiones)] ++ [()] -}