{- problema todosDigitosIguales (n:Z) : B  {
    requiere: {n > 0}
    asegura: {resultado=true ⟺ todos los dígitos de n son iguales}
}
-}

digitoUnidad ::Integer -> Integer
digitoUnidad x = mod x 10

todosDigitosIguales :: Integer -> Bool
todosDigitosIguales x  |  x < 10 = False 
                       | x == 11 = True
                       | ((todosDigitosIguales (div x 10)) == (div x 10)*10 + digitoUnidad x) = True
                       | otherwise = False