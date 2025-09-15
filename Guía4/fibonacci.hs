{-Implementar la función fibonacci:: Integer ->Integer que devuelve el i-´esimo número de Fibonacci.
Recordar que la secuencia de Fibonacci se define como:
   f ib(n) =
0 si n = 0
1 si n = 1
f ib(n − 1) + f ib(n − 2) en otro caso 

problema fibonacci (n: Z) : Z {
requiere: { n ≥ 0 }
asegura: { resultado = f ib(n) }
}
-}

--Fibonacci con Patern Matching
fibonacci :: Integer -> Integer
fibonacci 0 = 0
fibonacci 1 = 1
fibonacci n = fibonacci (n-1) + fibonacci (n-2)

--Fibonacci2, sin Patern Matching
 fibonacci2 :: Integer -> Integer
 fibonacci2 n  | n==0 = 0
              | n==1 = 1
              | otherwise = fibonacci2 (n-1) + fibonacci2 (n-2)