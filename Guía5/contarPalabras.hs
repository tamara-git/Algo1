{- contarPalabras :: [Char] -> Integer, que dada una lista de caracteres devuelve la cantidad de palabras que
tiene.-}

contarPalabras :: [Char] -> Integer
contarPalabras [] = 0
contarPalabras (x:xs) 