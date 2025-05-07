
componentesDistintas :: [(String,String)] -> Bool
componentesDistintas [] = True
componentesDistintas (x:[]) | fst x == snd x = False
                            | otherwise = True
componentesDistintas (x:xs) | fst x /= snd x = componentesDistintas (xs)
                            | otherwise = False

--necesito alguna función que me recorra la lista de tuplas
tuplasIguales :: (String,String) -> (String,String) -> Bool
tuplasIguales (a,b) (c,d) | a == c && b == d = True
                          | otherwise = False

sinTuplasRepetidas ::  [(String,String)] -> Bool
sinTuplasRepetidas [] = True
sinTuplasRepetidas (x:[]) = True
sinTuplasRepetidas (x:xs) | tuplasIguales x (head xs) == False = sinTuplasRepetidas (xs)
                          | otherwise = False

{-relacionesValidas :: [(String,String)] -> Bool
relacionesValidas [| componentesDistintas == True  && tuplasNoRepetidas == True = True
                                    | otherwise = False
-}