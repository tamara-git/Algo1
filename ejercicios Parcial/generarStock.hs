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

{-filtrarRepetidos :: [String] -> [String]
filtrarRepetidos (x:[]) = [x] 
filtrarRepetidos (pal:xs) | pertenece pal xs == True = pal: quitar pal xs
                          | otherwise = pal: filtrarRepetidos xs-}
                        
filtrarRepetidos :: String -> [String] -> [String]
filtrarRepetidos (x:[]) = [x] 
filtrarRepetidos palabra (pal:xs) | palabra == pal = palabra: quitar palabra xs
                                 | otherwise = pal: quitar palabra xs

cantidadRepeticiones :: String -> [String] -> Int
cantidadRepeticiones palabra (x:[]) = 0
cantidadRepeticiones palabra (pal:xs) | palabra == pal = 1 + cantidadRepeticiones (xs)
                                      | otherwise = cantidadRepeticiones (xs)
 
generarStock :: [String] -> [(String, Int)]
generarStock (x:[]) = [[x],0]
generarStock (x:xs) = [(filtrarRepetidos palabra (pal:xs), cantidadRepeticiones palabra (pal:xs) )]