esMultiploDe :: Integer -> Integer -> Bool
esMultiploDe x y = mod x y == 0
{-problema estanRelacionados (a:Z,b:Z) Bool {
  requiere: {a /= 0 y b /= 0}
  asegura: {(res = True) ↔ (a*a + a*b*k = 0 para algún k ∈ Z con k /= 0)}
} -}
estanRelacionados :: Integer -> Integer -> Boolz
estanRelacionados x y = esMultiploDe x y 

