type Relaciones = [(String,String)]

componentesDistintas :: Relaciones -> Bool
componentesDistintas [] = True
componentesDistintas [(palabra1,palabra2)] | palabra1 == palabra2 = False
                                           | otherwise = True

tuplasNoRepetidas :: Relaciones -> Relaciones -> Bool
tuplasNoRepetidas [] [] = True
tuplasNoRepetidas [(palabra1, palabra2)] [(palabra3, palabra4)] | (palabra1 == palabra3) && (palabra2 == palabra4) = False
                                                                 | otherwise = True
{-relacionesValidas :: Relaciones -> Bool
relacionesValidas [(palabra1,palabra2)] | componentesDistintas == True  && tuplasNoRepetidas == True = True
                                    | otherwise = False
-}