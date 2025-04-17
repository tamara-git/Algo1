{- problema todosDigitosIguales (n:Z) : B  {
    requiere: {n > 0}
    asegura: {resultado=true ⟺ todos los dígitos de n son iguales}
}
-}

todosDigitosIguales :: Integer -> Bool
todosDigitosIguales x  |  x < 10 = False 
                       | todosDigitosIguales (x- 1) 
                       | otherwise = False