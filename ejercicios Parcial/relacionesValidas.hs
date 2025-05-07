
componentesDistintas :: [(String,String)] -> Bool
componentesDistintas [] = True
componentesDistintas (x:[]) | fst x == snd x = False
                            | otherwise = True
componentesDistintas (x:xs) | fst x /= snd x = componentesDistintas (xs)
                            | otherwise = False

pertenece :: (String,String) -> [(String,String)] -> Bool
pertenece y [] = True
pertenece y (x:xs) | x == y = True
                   | otherwise = pertenece y (xs)

sinTuplasRepetidas ::  [(String,String)] -> Bool 
sinTuplasRepetidas [] = True
sinTuplasRepetidas (x:[]) = True
sinTuplasRepetidas (x:xs) | pertenece x xs == True = False
                          | otherwise = sinTuplasRepetidas (xs)
    
relacionesValidas :: [(String,String)] -> Bool
relacionesValidas (x:xs) | (sinTuplasRepetidas (x:xs) == True) && (componentesDistintas (x:xs) == True) = True
                         | otherwise = False
                              