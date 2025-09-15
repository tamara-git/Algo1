{-Dado un número entero mayor a 9, extrae su dígito de las decenas.-}
digitoDecenas :: Integer -> Integer
digitoDecenas z | z > 9 = div (mod z 100) 10  

{-digitoN_esimo :: Integer -> Integer
  digitoN_esimo x = div (mod x (10 ^ (i + 1))) (10 ^ i)
-}

