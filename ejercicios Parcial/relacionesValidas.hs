
componentesDistintas :: [(String,String)] -> Bool
componentesDistintas [] = True
componentesDistintas (x:[]) | fst x == snd x = False
                            | otherwise = True
componentesDistintas (x:xs) | fst x /= snd x = componentesDistintas (xs)
                            | otherwise = False


eliminarTuplasRepetidas :: [(String,String)] -> [(String,String)]
eliminarTuplasRepetidas (x:[]) = (x:[])
eliminarTuplasRepetidas (x:xs) | x == head xs = eliminarTuplasRepetidas (xs) 
                               | otherwise = x:eliminarTuplasRepetidas (xs)

{-relacionesValidas :: [(String,String)] -> Bool
relacionesValidas [| componentesDistintas == True  && tuplasNoRepetidas == True = True
                                    | otherwise = False
-}