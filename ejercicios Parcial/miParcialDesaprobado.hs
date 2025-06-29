{-Se dice que n es un número abundante si la suma de sus divisores propios es mayor que n. Los divisores propios de un número son todos los divisores sin contar al número mismo. Por ejemplo, los divisores propios de 12 son 1, 2, 3, 4 y 6. La suma de los divisores propios de 12 es 1 + 2 + 3 + 4 + 6 = 16, que es mayor que 12. Por lo tanto, 12 es un número abundante.

Se pide implementar cantidadNumerosAbundantes:

problema cantidadNumerosAbundantes (d: Z,h: Z) : Z {
  requiere: {0 < d ≤ h}
  asegura: {res es la cantidad de números abundantes en el rango [d..h]}
}

  Ejemplo: cantidadNumerosAbundantes 12 24 debe devolver 4-}



divisoresPropios :: Int -> Int -> [Int]
divisoresPropios n d | d >= n = []
                     | (d < n) && (mod n d == 0) = [d] ++ [divisoresPropios n (d+1)]
                     | otherwise = [divisoresPropios n (d+1)]

--sumarDivisores :: [Int] -> Int


--cantidadNumerosAbundantes :: Int -> Int -> Int 
--cantidadNumerosAbundantes d h 

