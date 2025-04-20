{- problema todosDigitosIguales (n:Z) : B  {
    requiere: {n > 0}
    asegura: {resultado=true ⟺ todos los dígitos de n son iguales}
}
-}

digitoUnidad :: Integer -> Integer
digitoUnidad x = mod x 10

cantDigitos :: Integer -> Integer
cantDigitos x | x == 0 = 0
              | x < 10 = 1
              | otherwise = cantDigitos (div x 10) + 1

todosDigitosIguales :: Integer -> Bool
todosDigitosIguales x  | x < 10 = True 
                       | x /= (div x 10) + (digitoUnidad (div x 10)) * 10**(cantDigitos (div x 10)) = False
                       | otherwise = todosDigitosIguales (div x 10)


todosDigitosIguales2 :: Integer -> Bool
todosDigitosIguales2 n
  | n < 100 && mod n 11== 0 = True
  | n < 10 = True
  | mod n 10 /= mod (div n 10) 10 = False
  | otherwise = todosDigitosIguales2 (div n 10)