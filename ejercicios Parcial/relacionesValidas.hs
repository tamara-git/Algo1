
componentesDistintas :: [(String,String)] -> Bool
componentesDistintas [] = True
componentesDistintas (x:[]) | fst x == snd x = False
                            | otherwise = True
componentesDistintas (x:xs) | fst x /= snd x = componentesDistintas (xs)
                            | otherwise = False


eliminartuplasRepetidas :: [(String,String)] -> [(String,String)]
eliminartuplasRepetidas (x:[]) = [x]
eliminartuplasRepetidas | x == head xs = eliminartuplasRepetidas (xs) 
                        | otherwise = x:eliminartuplasRepetidas (xs)

{-relacionesValidas :: [(String,String)] -> Bool
relacionesValidas [| componentesDistintas == True  && tuplasNoRepetidas == True = True
                                    | otherwise = False
-}