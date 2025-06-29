{-Se dice que n es un número abundante si la suma de sus divisores propios es mayor que n. Los divisores propios de un número son todos los divisores sin contar al número mismo. Por ejemplo, los divisores propios de 12 son 1, 2, 3, 4 y 6. La suma de los divisores propios de 12 es 1 + 2 + 3 + 4 + 6 = 16, que es mayor que 12. Por lo tanto, 12 es un número abundante.

Se pide implementar cantidadNumerosAbundantes:

problema cantidadNumerosAbundantes (d: Z,h: Z) : Z {
  requiere: {0 < d ≤ h}
  asegura: {res es la cantidad de números abundantes en el rango [d..h]}
}

  Ejemplo: cantidadNumerosAbundantes 12 24 debe devolver 4-}

esDivisor :: Int -> Int -> [Int]
esDivisor n i | i >= n = []
              | (i < n) && (mod n i == 0) = i:esDivisor n (i+1)
              | otherwise = esDivisor n (i+1)


divisoresPropios :: Int -> [Int]
divisoresPropios n = esDivisor n 1


sumarDivisores :: [Int] -> Int
sumarDivisores [x] = x
sumarDivisores (x:xs) = x + sumarDivisores xs 


esNumeroAbundante :: Int -> Bool 
esNumeroAbundante n | sumarDivisores (divisoresPropios n) > n = True  
                    | otherwise = False  

cantidadNumerosAbundantes :: Int -> Int -> Int
cantidadNumerosAbundantes d h | d > h = 0   
                              | (d <= h) && (esNumeroAbundante d == True) = 1 + cantidadNumerosAbundantes (d + 1) h 
                              | otherwise = cantidadNumerosAbundantes (d + 1) h
