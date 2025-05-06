
componentesDistintas :: [(String,String)] -> Bool
componentesDistintas [] = True
componentesDistintas (x:[]) | fst x == snd x = False
                            | otherwise = True
componentesDistintas (x:xs) | fst x /= snd x = componentesDistintas (xs)
                            | otherwise = False

tuplasNoRepetidas :: [(String,String)] -> Bool
tuplasNoRepetidas [] = True
tuplasNoRepetidas (x:[]) = True
tuplasNoRepetidas (x:xs) | x /= head xs = tuplasNoRepetidas (tail xs) 
                         | otherwise = False

{-relacionesValidas :: Relaciones -> Bool
relacionesValidas [(palabra1,palabra2)] | componentesDistintas == True  && tuplasNoRepetidas == True = True
                                    | otherwise = False
-}