

esCapicua :: Integer -> Bool
esCapicua x  | x <= 10 = False 
             | mod x 10 == 0 = False
             | esCapicua (x-1) + (x-(x-1)) = True 
