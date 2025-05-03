type relaciones = [(String,String)]

componentesDistintas :: relaciones -> Bool
componentesDistintas [(palabra1,palabra2)] | palabra1 == palabra2 = False
                                           | otherwise = True

tuplasNoRepetidas :: relaciones -> relaciones 
tuplasNoRepetidas [(palabra1, palabra2)] [(palabra3, palabra4)] | fst [(palabra1,palabra2)] == fst [(palabra3,palabra4)] && snd [(palabra1,palabra2)] == snd [(palabra3,palabra4)] = False
                                                                | otherwise = True
relacionesValidas :: relaciones -> Bool
relacionesValidas [(String,String)] | componentesDistintas && tuplasNoRepetidas == True = True
                                    | otherwise = False
