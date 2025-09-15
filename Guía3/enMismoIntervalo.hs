{-dados dos números reales, indica si están relacionados por la relación de equivalencia
en R cuyas clases de equivalencia son (-∞,3], (3,7] y (7,∞), o dicho de otra manera,
si pertenecen al mismo intervalo-}

intervalo :: Float -> Char
intervalo x | (x <= 3) = 'A'
            | (x > 3) && (x <= 7) = 'B'
            | (x > 7) = 'C'


enMismoIntervalo :: Float -> Float -> Bool
enMismoIntervalo x y = intervalo x == intervalo y