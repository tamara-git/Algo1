Intervalo :: Float -> Char
Intervalo x | (x <= 3) = 'A'
            | (x > 3 && x <= 7 ) = 'B'
            | ( x > 7) = 'C'

enMismoIntervalo :: Float -> Float -> Char -> Bool
enMismoIntervalo x y  | (Intervalo x == Intervalo y) = True
                      | otherwise = False