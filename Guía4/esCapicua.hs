--Hecho en clase.

dígitoUnidades :: Integer -> Integer
dígitoUnidades x = mod x 10

cantidadDígitos :: Integer -> Integer
cantidadDígitos x | x == 0 = 0
              | x < 10 = 1
              | otherwise = cantidadDígitos (div x 10) + 1

sacarÚltimoDígito :: Integer -> Integer
sacarÚltimoDígito n
              | n < 0 = -sacarÚltimoDígito (-n)
              | otherwise =  div n 10

invertir :: Integer -> Integer
invertir n | n < 0     = -invertir (-n)
           | n < 10    = n
           | otherwise = dígitoUnidades n * (10 ^ (cantidadDígitos n - 1)) + invertir (sacarÚltimoDígito n)

esCapicúaBien :: Integer -> Bool
esCapicúaBien n = n == invertir n

--Clase 21/04
cantidadDigitos :: Integer -> Integer
cantidadDigitos x | x == 0 = 0
              | x < 10 = 1
              | otherwise = cantidadDigitos (div x 10) + 1

iesimoDigito :: Integer -> Integer
iesimoDigito n i = mod (div n 10^(cantidadDigitos (n)-i) 10)

esCapicua :: Integer -> Bool
esCapicua n | n < 10 = True
            | esCapicua (div )