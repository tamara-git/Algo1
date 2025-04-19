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
                       | x == (div x 10)*10 + digitoUnidad x = (todosDigitosIguales (div x 10))
                       | otherwise = False