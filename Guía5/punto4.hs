{-sacarBlancosRepetidos :: [Char] -> [Char], que reemplaza cada subsecuencia de blancos contiguos de la pri-
mera lista por un solo blanco en la lista resultado.-}

sacarBlancosRepetidos :: [Char] -> [Char]
sacarBlancosRepetidos [] = []
sacarBlancosRepetidos [x] = [x]
sacarBlancosRepetidos (x:y:xs) | (x == ' ') && (y == ' ') = sacarBlancosRepetidos (y:xs)
                                 | (x /= ' ') && (y /= ' ') = x:y:sacarBlancosRepetidos (xs)
                                 | otherwise = x:sacarBlancosRepetidos(y:xs)

{-contarPalabras :: [Char] -> Integer, que dada una lista de caracteres devuelve la cantidad de palabras que
tiene.-}

sacarBlancosAlInicio :: [Char] -> [Char]
sacarBlancosAlInicio (x:xs) | x == ' ' = sacarBlancosAlInicio xs 
                            | otherwise = (x:xs)

ultimo :: [Char] -> Char
ultimo [x] = x 
ultimo (x:xs) = ultimo xs 

principio :: [Char] -> [Char]
principio [x] = []
principio (x:xs) = [x] ++ principio xs 

sacarBlancosAlFinal :: [Char] -> [Char]
sacarBlancosAlFinal (x:xs) | ultimo (x:xs) == ' ' = sacarBlancosAlFinal (principio (x:xs))
                           | otherwise = (x:xs)

limpiarSecuencia :: [Char] -> [Char]
limpiarSecuencia (x:xs) = sacarBlancosRepetidos(sacarBlancosAlFinal (sacarBlancosAlInicio (x:xs)))

contarPalabrasAux :: [Char] -> Integer 
contarPalabrasAux [x] = 1 
contarPalabrasAux (x:xs) | x /= ' ' = 0 + contarPalabrasAux xs
                      | otherwise = 1 + contarPalabrasAux xs

contarPalabras :: [Char] -> Integer
contarPalabras (x:xs) = contarPalabrasAux (limpiarSecuencia (x:xs))

{-palabras :: [Char] -> [[Char]], que dada una lista arma una nueva lista con las palabras de la lista original.-}

armarPalabra :: [Char] -> [Char]
armarPalabra (x:xs) | x /= ' ' = [x] ++ armarPalabra xs
                    | otherwise = []

quitarPrimerPalabra :: [Char] -> [Char]
quitarPrimerPalabra [x] | x /= ' ' = []
                        | otherwise = []
quitarPrimerPalabra (x:xs) | x /= ' ' = [] ++ quitarPrimerPalabra xs 
                           | otherwise = xs

obtenerPrimerPalabra :: [Char] -> [Char]
obtenerPrimerPalabra [x] = [x]
obtenerPrimerPalabra (x:xs) | x /= ' ' = [x] ++ obtenerPrimerPalabra xs 
                            | otherwise = []

palabrasAux :: [Char] -> [[Char]]
palabrasAux [] = []
palabrasAux (x:xs) = [obtenerPrimerPalabra (x:xs)] ++ palabrasAux (quitarPrimerPalabra (x:xs))

palabras :: [Char] -> [[Char]]
palabras (x:xs) = palabrasAux((limpiarSecuencia(x:xs)))