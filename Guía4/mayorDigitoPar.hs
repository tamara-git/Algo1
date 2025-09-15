{-problema mayorDigitoPar (n: N) : N {
requiere: { True }
asegura: {resultado es el mayor de los dígitos pares de n. 
Si n no tiene ningún dígito par, entonces resultado es -1.}
}-}

digitoUnidad :: Integer -> Integer
digitoUnidad n = mod n 10


listarDigitosPares :: Integer -> [Integer]
listarDigitosPares n | n < 10 && (mod n 2 == 0) = [n]
                     | n < 10 && (mod n 2 /= 0) = []
                     | n >= 10 && (mod (digitoUnidad n) 2 == 0) = [digitoUnidad n] ++ listarDigitosPares (div n 10)
                     | otherwise = listarDigitosPares (div n 10)


extraerMayorPar :: [Integer] -> Integer
extraerMayorPar [x] | mod x 2 == 0 = x
                    | otherwise = -1
extraerMayorPar (x:xs) | x > extraerMayorPar xs = x
                       | otherwise = extraerMayorPar xs


mayorDigitoPar :: Integer -> Integer
mayorDigitoPar n = extraerMayorPar (listarDigitosPares n)