{-Dado un número entero, extrae su dígito de las unidades.-}
digitoUnidades :: Integer -> Integer
digitoUnidades x = mod x 10