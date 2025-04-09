--dados dos números racionales, decide si alguno es igual a 0 (resolverlo con y sin pattern matching)
algunoEsCero ::  Float -> Float -> Bool
algunoEsCero x y | x == 0 = True
                 | y == 0 = True 
                 | otherwise = False

--Con Pattern Matching
algunoEsCero2 :: Float -> Float -> Bool
algunoEsCero2 0 0= True
algunoEsCero2 x y = False

