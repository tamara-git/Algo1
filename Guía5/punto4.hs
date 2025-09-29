{-sacarBlancosRepetidos :: [Char] -> [Char], que reemplaza cada subsecuencia de blancos contiguos de la pri-
mera lista por un solo blanco en la lista resultado.-}

sacarBlancosRepetidos :: [Char] -> [Char]
sacarBlancosRepetidos [] = []
sacarBlancosRepetidos [x] = [x]
sacarBlancosRepetidos (x:y:z:xs) | (x == ' ') && (y == ' ') = sacarBlancosRepetidos (y:xs)
                                 | otherwise = x:y:sacarBlancosRepetidos(xs)