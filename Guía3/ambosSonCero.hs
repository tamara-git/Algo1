{-dados dos número racionales, decide si ambos son iguales a 0-}
ambosSonCero ::  Float -> Float -> Bool
ambosSonCero x y | (x == 0) & (y == 0) = True
                 | otherwise = False

-- Con Pattern Matching

ambosSonCeroPattern :: Float -> Float -> Bool
ambosSonCeroPattern 0 0 = True
ambosSonCeroPattern x y = False