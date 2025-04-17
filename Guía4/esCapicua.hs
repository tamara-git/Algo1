esCapicua :: Integer -> Bool
esCapicua x  | x < 10 = False 
             | otherwise = esCapicua (x-1) + 1 = True
