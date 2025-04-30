{-sacarBlancosRepetidos :: [Char] -> [Char], que reemplaza cada subsecuencia de blancos contiguos 
de la primera lista por un solo blanco en la lista resultado.-}


sacarBlancosRepetidos :: [Char] -> [Char]
sacarBlancosRepetidos [] = []
sacarBlancosRepetidos [x] = [x]
sacarBlancosRepetidos (x:y:xs) | x == ' ' && y== ' ' = sacarBlancosRepetidos (xs)
                               | otherwise = x : sacarBlancosRepetidos(y:xs)

sacarBlancosInicio :: [Char] -> [Char]
sacarBlancosInicio [] = []
sacarBlancosInicio [x] = [x]
sacarBlancosInicio (x:xs) | x == ' ' = sacarBlancosInicio (xs)
                          | otherwise = (x:xs)

sacarBlancoFinal :: [Char] -> [Char]
sacarBlancoFinal (x:xs) = reverso (sacarBlancosInicio(reverso (x:xs)))
