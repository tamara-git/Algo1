ambosSonCero ::  Float -> Float -> Bool
ambosSonCero x y |  (x==0 = True) && (y==0 = True)
                 | otherwise = False

--Con Pattern Matching
algunoEsCero2 :: Float -> Float -> Bool
algunoEsCero2 x 0 = True
algunoEsCero2 0 y = True
algunoEsCero2 x y = False
--Con Pattern Matching
algunoEsCero2 :: Float -> Float -> Bool
algunoEsCero2 x 0 = True
algunoEsCero2 0 y = True
algunoEsCero2 x y = False
                 | otherwise = False

--Con Pattern Matching
ambosSonCero :: Float -> Float -> Bool
ambosSonCero x y = 0 0