{- Implementar la función esSumaInicialDePrimos :: Integer -> Bool según la siguiente especificación:
problema esSumaInicialDePrimos (n: Z) : B {
requiere: { n ≥ 0 }
asegura: { resultado = true ↔ n es igual a la suma de los m primeros n´umeros primos, para algún m.}
}-}

menorDivisorDesde :: Integer -> Integer -> Integer
menorDivisorDesde x d | mod x d == 0 = d
                      | otherwise = menorDivisorDesde x (d+1)

menorDivisor :: Integer -> Integer 
menorDivisor x = menorDivisorDesde x 2 

esPrimo :: Integer -> Bool
esPrimo x | menorDivisor x == x = True
          | otherwise = False

sumaInicialDePrimos :: Integer -> Integer -> Integer
sumaInicialDePrimos desde hasta | esPrimo desde == False = 0 + sumaInicialDePrimos (desde+1) hasta
                                   | (desde <= hasta) && (esPrimo desde == True) = desde + sumaInicialDePrimos (desde + 1) hasta
                                   | otherwise = 0

esSumaInicialDePrimosAux :: Integer -> Integer -> Bool
esSumaInicialDePrimosAux n hasta | n < 2 = False
                                 | n < hasta = False
                                 | n /= sumaInicialDePrimos 2 (hasta) = esSumaInicialDePrimosAux n (hasta + 1)
                                 | otherwise = True

esSumaInicialDePrimos :: Integer -> Bool
esSumaInicialDePrimos n = esSumaInicialDePrimosAux n 2