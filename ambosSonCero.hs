ambosSonCero ::  Float -> Float -> Bool
ambosSonCero x y |  (x==0 && y==0) = True
                 | otherwise = False

--Con Pattern Matching
ambosSonCero2 :: Float -> Float -> Bool
ambosSonCero2 0 0 = True
ambosSonCero2 x y = False