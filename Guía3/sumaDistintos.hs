{-Dados tres números enteros, calcula la suma sin sumar repetidos (si los hubiera).-}

sonIguales :: Integer -> Integer -> Bool
sonIguales x y | x == y = True
               | otherwise = False

hayIgualdad :: Integer -> Integer -> Integer -> Bool
hayIgualdad x y z | sonIguales x y || sonIguales x z || sonIguales y z= True
                  | otherwise = False 

sumaDistintos :: Integer -> Integer -> Integer -> Integer
sumaDistintos x y z | sonIguales x y || sonIguales y z = x + z
                    | sonIguales x z = x + y






















{-

sumaDos :: Integer -> Integer -> Integer
sumaDos x y | x /= y = x+y
            | otherwise = x

sumaDistintos :: Integer -> Integer -> Integer -> Integer
sumaDistintos x y z = sumaDos (sumaDos x y) z


-}