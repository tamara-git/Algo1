
componentesDistintas :: [(String,String)] -> Bool
componentesDistintas [] = True
componentesDistintas (x:[]) | fst x == snd x = False
                            | otherwise = True
componentesDistintas (x:xs) | fst x /= snd x = componentesDistintas (xs)
                            | otherwise = False

tuplasNoRepetidas :: [(String,String)] -> Bool
tuplasNoRepetidas [] = True
tuplasNoRepetidas (x:[]) = True
tuplasNoRepetidas (x:y:xs) | x == head xs = False
                         | otherwise = tuplasNoRepetidas (xs)

{-relacionesValidas :: [(String,String)] -> Bool
relacionesValidas [| componentesDistintas == True  && tuplasNoRepetidas == True = True
                                    | otherwise = False
-}