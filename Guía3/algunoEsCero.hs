--dados dos números racionales, decide si alguno es igual a 0 (resolverlo con y sin pattern matching)
algunoEsCero ::  Float -> Float -> Bool
algunoEsCero x y | x == 0 || (y == 0) = True
                 | otherwise = False

--Con Pattern Matching
algunoEsCeroPattern :: Float -> Float -> Bool
algunoEsCeroPattern x 0 = True
algunoEsCeroPattern 0 y = True
algunoEsCeroPattern x y = False

