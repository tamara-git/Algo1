Intervalo :: Float -> Bool
Intervalo x  | x <= 3
             | 3 < x <= 7
             | x > 7

enMismoIntervalo :: Float -> Float -> Bool
enMismoIntervalo x y | Intervalo x == Intervalo y = True
                     | otherwise = False