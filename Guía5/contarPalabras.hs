{- contarPalabras :: [Char] -> Integer, que dada una lista de caracteres devuelve la cantidad de palabras que
tiene.-}

reverso :: [t] -> [t]
reverso [] = []
reverso [x] = [x]
reverso (x:xs) = reverso (xs) ++ [x]

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

cantidadBlancos :: [Char] -> Integer
cantidadBlancos [] = 0
cantidadBlancos [x] = 0
cantidadBlancos (x:xs) | x == ' ' = 1
                       | otherwise = cantidadBlancos (xs)
{-contarPalabras :: [Char] -> Integer
contarPalabras [] = 0
contarPalabras (x:xs) | x == ' ' = contarPalabras (xs)
                      | otherwise = 
                    -}