{-Lo cual resulta en la siguiente definición recursiva: a1 = 2, an = 2 + 1/an−1.
 Utilizando esta sucesión, especificar e implementar una función raizDe2Aprox :: Integer -> Float 
 que dado n ∈ N devuelva la aproximación de √2 definida por √2 ≈ an −1.
Por ejemplo:
raizDe2Aprox 1 ⇝ 1
raizDe2Aprox 2 ⇝ 1,5
raizDe2Aprox 3 ⇝ 1,4 -}
{-problema raizDe2Aprox (n:Z) : R {
    requiere: {n ∈ N}
    asegura: {resultado = √2 ≈ an−1}
 }
-}


--Recursión 
an :: Integer -> Float 
an 1 = 2
an n = 2 + 1 / an (n-1) 

-- Uso la recursión y le resto uno 
raizDe2Aprox :: Integer -> Float
raizDe2Aprox n = (an n) -1 