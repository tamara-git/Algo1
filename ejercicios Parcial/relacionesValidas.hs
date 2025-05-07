
componentesDistintas :: [(String,String)] -> Bool
componentesDistintas [] = True
componentesDistintas (x:[]) | fst x == snd x = False
                            | otherwise = True
componentesDistintas (x:xs) | fst x /= snd x = componentesDistintas (xs)
                            | otherwise = False


eliminarTuplasRepetidas :: [(String,String)] -> [(String,String)]
eliminarTuplasRepetidas (x:[]) = (x:[])
eliminarTuplasRepetidas (x:y:xs) | x == y = eliminarTuplasRepetidas (y:xs) 
                               | otherwise = x:eliminarTuplasRepetidas (y:xs)

{-relacionesValidas :: [(String,String)] -> Bool
relacionesValidas [| componentesDistintas == True  && tuplasNoRepetidas == True = True
                                    | otherwise = False
-}