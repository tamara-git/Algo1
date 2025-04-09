{-espeficación: problema f (n:Z) : Z {
requiere: {n=8 v n=16 v n=131}
asegura: {(n=8 -> res=16) y (n=16 -> res=4) y (n=131 -> res=1)} -}
f :: Integer -> Integer
g(8)= 16
g(16)=4
g(131)=1
