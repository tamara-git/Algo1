ambosSonCero ::  Float -> Float -> Bool
ambosSonCero x y |  (x==0 = True) && (y==0 = True)
                 | otherwise = False

--Con Pattern Matching
ambosSonCero2 :: Float -> Float -> Bool
ambosSonCero2 x y = 0 0