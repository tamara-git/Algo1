intervalo :: Float -> Char
intervalo x | (x <= 3) = 'A'
            | (x > 3) && (x <= 7 ) = 'B'
            | ( x > 7) = 'C'

enMismoIntervalo :: Float -> Float -> Bool
enMismoIntervalo x y  = (intervalo x == intervalo y)
                      | otherwise = False                     