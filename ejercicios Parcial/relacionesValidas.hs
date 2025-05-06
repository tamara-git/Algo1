 

componentesDistintas :: [(String,String)] -> Bool
componentesDistintas [] = True
componentesDistintas (x:[]) | fst x == snd x = False
                            | otherwise = True
componentesDistintas (x:xs) | fst x /= snd x = True 
                            | otherwise = componentesDistintas (xs)

{-tuplasNoRepetidas :: [(String,String)] -> [(String,String)] -> Bool
tuplasNoRepetidas [] [] = True
tuplasNoRepetidas [(a,b)] [(c,d)] | tuplasNoRepetidas
                               | otherwise = 
-}
{-relacionesValidas :: Relaciones -> Bool
relacionesValidas [(palabra1,palabra2)] | componentesDistintas == True  && tuplasNoRepetidas == True = True
                                    | otherwise = False
-}