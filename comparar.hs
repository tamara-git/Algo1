{-problema comparar (a : Z, b : Z) : Z {
requiere: {T rue}
asegura: {(res = 1) ↔ (sumaUltimosDosDigitos(a) < sumaUltimosDosDigitos(b))}
asegura: {(res = −1) ↔ (sumaUltimosDosDigitos(a) > sumaUltimosDosDigitos(b))}
asegura: {(res = 0) ↔ (sumaUltimosDosDigitos(a) = sumaUltimosDosDigitos(b))}
}

problema sumaUltimosDosDigitos (x : Z) : Z {
   requiere: {True}
   asegura: {res = (|x| mod 10) + (|x|/10 mod 10)}
}

Por ejemplo:
comparar 45 312 ⇝ -1 porque 45 ≺ 312 y 4 + 5 > 1 + 2.
comparar 2312 7 ⇝ 1 porque 2312 ≺ 7 y 1 + 2 < 0 + 7.
comparar 45 172 ⇝ 0 porque no vale 45 ≺ 172 ni tampoco 172 ≺ 45. -}

sumaUltimosDosDigitos :: Integer -> Integer
sumaUltimosDosDigitos x = (mod x 10) +  mod ((div x 10) 10)

comparar :: Integer -> Integer -> Integer
comparar a b  | sumaUltimosDosDigitos a < sumaUltimosDosDigitos b = 1
              | sumaUltimosDosDigitos a > sumaUltimosDosDigitos b = -1
              | sumaUltimosDosDigitos a == sumaUltimosDosDigitos b = 0
              

