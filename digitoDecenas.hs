{-Dado un número entero mayor a 9, extrae su dígito de las decenas.-}
digitoDecenas :: Integer -> Integer
digitoDecenas x =  div (mod x 100)  10