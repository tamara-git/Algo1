{- problema medioFact (n:Z) :Z  {
    requiere: {n >= 0}
    asegura: {resultado = productoria i=0  [(n-1)/2]  (n-2i)}
}
-}

medioFact :: Integer -> Integer
medioFact 0 = 1
medioFact n = medioFact (n-2) * n 
