{-Especificar e implementar la función sumaDigitos :: Integer -> Integer que calcula la suma de dígitos de
un número natural. Para esta función pueden utilizar div y mod.-}

digitoUnidad :: Integer -> Integer
digitoUnidad n = mod n 10


sumaDigitos :: Integer -> Integer
sumaDigitos n | n < 10 = n
              | otherwise = digitoUnidad n + sumaDigitos (div n 10) 
