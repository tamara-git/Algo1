{-problema mayorDigitoPar (n: N) : N {
requiere: { True }
asegura: { resultado es el mayor de los dígitos pares de n. 
Si n no tiene ningún dígito par, entonces resultado es -1.}
}-}



mayorDigitoPar :: Integer -> Integer
mayorDigitoPar n | (n < 10 ) && (mod n 2 == 1) = -1
                 | (n < 10 ) && (mod n 2 == 0) = n
                 | otherwise = (mayorDigitoPar (div n 2))*2 