type Terna = (Integer, Integer, Integer)
{-problema todosMenores (t: ZxZxZ) : Bool {
    requiere: {True}
    asegura: {(res=true) ↔ (f(t0) > g(t0) ∧ (f(t1) > g(t1)) ∧ (f(t2) > g(t2)))}
}-}
todosMenores :: Terna -> Bool
todosMenores (a,b,c) = (f(a) > g(a)) && (f(b) > g(b)) && (f(c) > g(c))

{-problema f (n:Z) : Z {
    requiere: {True}
    asegura: {(n <= 7 →  res = n*2) ∧ (n > 7 →  res= 2n-1 )
} -}
f :: Integer -> Integer
f n | n <= 7 = n*2
    | n > 7 = 2*n - 1

{- problema g (n:Z) : Z {
    requiere: {True}
    asegura: {Si n es un número par entonces res = n/2, en caso contrario, res = 3n+1}
} -}
g :: Integer -> Integer
g n |  mod n 2 == 0 = div n 2
    | otherwise = 3*n + 1
