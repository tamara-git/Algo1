{-Especificar e implementar la función sumaDigitos :: Integer -> Integer que calcula la suma de dígitos de
un número natural. Para esta función pueden utilizar div y mod.-}

digitoUnidad :: Integer -> Integer
digitoUnidad x = mod x 10

cantidadDigitos :: Integer -> Integer
cantidadDigitos x | x == 0 = 0
                  | x < 10 = 1
                  | otherwise = cantidadDigitos (div x 10) + 1

sumaDigitos :: Integer -> Integer
sumaDigitos n | cantidadDigitos n == 1 = n 
              | otherwise = sumaDigitos (div n 10) + digitoUnidad n 