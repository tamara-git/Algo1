


esCapicua :: Integer -> Bool
esCapicua x  | x < 10 = True 
             | mod x 10 == 0 = False 
             | 