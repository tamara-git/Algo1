{- problema todosDigitosIguales (n:Z) : B  {
    requiere: {n > 0}
    asegura: {resultado=true ⟺ todos los dígitos de n son iguales}
}
-}

decena :: Integer -> Integer
decena x = 10*x

todosDigitosIguales :: Integer -> Bool
todosDigitosIguales x  |  x < 10 = False 
                       | otherwise = todosDigitosIguales (x - div (x 2)) + div x 2)