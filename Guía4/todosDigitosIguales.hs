{- problema todosDigitosIguales (n:Z) : B  {
    requiere: {n > 0}
    asegura: {resultado=true ⟺ todos los dígitos de n son iguales}
}
-}

CantDigitos :: 

CantDigitos :: Integer -> Bool
CantDigitos x =  
--todosDigitosIguales :: Integer -> Bool
todosDigitosIguales x  | x < 10 = True 
                       | x == 11 = True
                       | x == (div x 10)*10 + digitoUnidad x = (todosDigitosIguales (div x 10)) = True


todosDigitosIguales2 :: Integer -> Bool
todosDigitosIguales2 n
  | n < 100 = True
  | mod n 10 /= mod (div n 10) 10 = False
  | otherwise = todosDigitosIguales2 (div n 10)