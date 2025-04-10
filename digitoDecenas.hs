{-Dado un número entero mayor a 9, extrae su dígito de las decenas.-}
digitoDecenas :: Integer -> Integer
digitoDecenas x =  div ((div x 10)* 10)  10