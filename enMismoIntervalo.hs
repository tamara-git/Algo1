Intervalo :: Float -> Char
Intervalo x | (x <= 3) = ClaseEquivalencia1
            | (3 < x <= 7) = ClaseEquivalencia2
            | ( x > 7) = ClaseEquivalencia3

enMismoIntervalo :: Float -> Float -> Char -> Bool
enMismoIntervalo x y  | (Intervalo x == Intervalo y) = True
                      | otherwise = False