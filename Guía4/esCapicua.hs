esCapicua :: Integer -> Bool
esCapicua x  | x < 10 = False 
             | x == 10 = 01
             | esCapicua (x-1) = True 
