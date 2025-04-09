{- A partir de las funciones definidas en a y b, implementar las funciones parciales h=fog y k=gof -}
f :: Integer -> Integer
f(1)=8
f(4)=131
f(16)=16

g :: Integer -> Integer
g(8)= 16
g(16)=4
g(131)=1

h :: Integer -> Integer
h= f.g

k :: Integer -> Integer
k = g.f
