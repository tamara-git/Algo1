{- problema bisiesto (año:Z) : Bool {
    requiere: {True}
    asegura: {(res=false) ↔ (año no es múltiplo de 4, o bien, año es múltiplo de 100 pero no de 400)
} -}
type Anio = Integer
type EsBisiesto = Bool

bisiesto :: Integer -> Bool 
bisiesto x = not ((mod x 4 /= 0) && (mod x 100 == 0) && (mod x 400 /= 0))