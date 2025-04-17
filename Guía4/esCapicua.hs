esCapicua :: Integer -> Bool
 esCapicua x  | x < 10 = False 
             | esCapicua (esCapicua (x-1)) + 1 = True
