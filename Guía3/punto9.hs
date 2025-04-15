{- problema f1 (n:R) : R {
  requiere: {True}
  asegura: {Si n = 0 entonces res = 1, en caso contrario, res = 0}
}  -}
f1 :: Float -> Float
f1 n | n == 0 = 1
| otherwise = 0  

{-problema f2 (n:R) : R  {
  requiere: {True}
  asegura: {(n = 1 → res = 15) ∧ (n = -1 →  res= -15)
} -}
f2 :: Float -> Float
f2 n | n == 1 = 15
| n == -1 = -15

{-problema f3 (n:R) : R  {
  requiere: {True}
  asegura: {(n <= 9 → res = 7) ∧ (n >= 3 → res= 5)}
} -}
f3 :: Float -> Float
f3 n | n <= 9 = 7
| n >= 3 = 5

{-problema f4 (x:R, y:R) : R {
  requiere: {True}
  asegura: {res= (x + y)/2 }
} -}
f4 :: Float -> Float -> Float
f4 x y = ( x + y )/2

{-problema f5 (P: RxR) : R {
  requiere: {True}
  asegura: {res = (p0 + p1)/2} 
}  -}
f5 :: ( Float , Float ) -> Float
f5 (x , y ) = ( x + y )/2

{-problema f6 (a: R, b: Z) : Bool {
  requiere: {True}
  asegura: {res = True  ⇔  truncate(a) = b}
} -}
--convierte un Float en un número entero, eliminando la parte decimal.
f6 :: Float -> Int -> Bool
f6 a b = truncate a == b
