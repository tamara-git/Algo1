{-
    requiere: {True}
    asegura: {res = sumatoria i=1 n (sumatoria j=1 m  q^(i+j)) }
-}

--Hecho por mí
sumaPotenciasDeJ :: Integer -> Integer -> Integer -> Integer
sumaPotenciasDeJ q j m | j <= m =  q^(j) + sumaPotenciasDeJ q (j+1) m
                       | otherwise = 0


sumaPotenciasDesde1Hastam :: Integer -> Integer -> Integer
sumaPotenciasDesde1Hastam q m = sumaPotenciasDeJ q 1 m 


sumaPotenciasDeI :: Integer -> Integer -> Integer -> Integer -> Integer
sumaPotenciasDeI q i n m | i <= n = (q^i)*(sumaPotenciasDesde1Hastam q m) + sumaPotenciasDeI q (i+1) n m
                         | otherwise = 0

                         
sumaPotenciasDesdeIHastaN :: Integer -> Integer -> Integer -> Integer
sumaPotenciasDesdeIHastaN q n m = sumaPotenciasDeI q 1 n m


sumaPotencias :: Integer -> Integer -> Integer -> Integer
sumaPotencias q n m = sumaPotenciasDesdeIHastaN q n m 


--Hecho en clase
sumatoriaInterna :: Integer -> Integer -> Integer -> Integer
sumatoriaInterna q n m  | m == 1 = q^(n+m)
                        | otherwise = q^(n+m) + sumatoriaInterna q n (m-1)

sumaPotenciasClase :: Integer -> Integer -> Integer -> Integer
sumaPotenciasClase q n m | n == 1 = sumatoriaInterna q n m
                    | otherwise = sumatoriaInterna q n m + sumaPotenciasClase q (n-1) m 