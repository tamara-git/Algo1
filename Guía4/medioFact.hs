{- problema medioFact (n:Z) :Z  {
    requiere: {n >= 0}
    asegura: {resultado = productoria i=0  [(n-1)/2]  (n-2i)}
}
-}

{-medioFactAux :: Integer -> Integer -> Integer
medioFactAux n i | i == 0 = n 
                 | i <= (n-1)/2 = (n-2i) * medioFactAux () 
-}























medioFact :: Integer -> Integer
medioFact 0 = 1
medioFact 1 = 1
medioFact n = medioFact (n-2) *  n