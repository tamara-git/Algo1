{- problema todosDigitosIguales (n:Z) : B  {
    requiere: {n > 0}
    asegura: {resultado=true ⟺ todos los dígitos de n son iguales}
}
-}

digitoUnidad :: Integer -> Integer
digitoUnidad n = mod n 10  

todosDigitosIguales :: Integer -> Bool
todosDigitosIguales n | n < 10 = True
                      | digitoUnidad n /= digitoUnidad (div n 10) = False
                      | otherwise = todosDigitosIguales (div n 10)  