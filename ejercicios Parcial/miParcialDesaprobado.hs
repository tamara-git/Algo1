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

{-Representaremos una cursada aprobada con una tupla String x Z x Z, donde:
La primera componente de la tupla contiene el nombre de una materia
La segunda componente de la tupla contiene el año de aprobación de la cursada
La tercera componente de la tupla contiene el cuatrimestre de aprobación de la cursada (el valor 0 representa un curso de verano)
Se pide implementar cursadasVencidas, que dada una lista de cursadas devuelva aquellas materias cuya aprobación de la cursada ya venció, y por lo tanto ya no se puede rendir el final
problema cursadasVencidas (s: seq⟨String x Z x Z⟩) :seq⟨String⟩ {
  requiere: { s[i]1 ≥ 1993 para todo i tal que 0 ≤ i < |s|}
  requiere: { 0 ≤ s[i]2 ≤ 2 para todo i tal que 0 ≤ i < |s|}
  asegura: { res no tiene elementos repetidos}
  asegura: { res contiene los nombres de todas las materias incluídas en s tales que la materia fue aprobada a más tardar en el primer cuatrimestre de 2021, inclusive}
  asegura: { res contiene solamente los nombres de las materias incluídas en s tales que la materia fue aprobada a más tardar en el primer cuatrimestre de 2021, inclusive}
}

    Ejemplo: cursadasVencidas [("Algoritmos y Estructuras de Datos I", 2020, 2), ("Algoritmos y Estructuras de Datos II", 2022, 1)] debe devolver ["Algoritmos y Estructuras de Datos I"]
    -}


accederAElemPorIndice :: [([Char], Int, Int)] -> Int -> ([Char], Int, Int)
accederAElemPorIndice [x] 1 = x 
accederAElemPorIndice (x:xs) 1 = x
accederAElemPorIndice (x:xs) i = accederAElemPorIndice xs (i-1)

fstTrupla :: ([Char], Int, Int) -> Int 
fstTrupla (a,b,c) = a

sndTrupla :: ([Char], Int, Int) -> Int 
sndTrupla (a,b,c) = a

third :: ([Char], Int, Int) -> Int 
third (a,b,c) = c 


cursadasVencidas :: [([Char], Int, Int)] -> Int -> [[Char]]
cursadasVencidas [x] 1 | (sndTrupla x) < 2021 = [fstTrupla (accederAElemPorIndice [x] 1)]
                       | otherwise = []
cursadasVencidas (x:xs) i | sndTrupla x < 2021 = [fstTrupla (accederAElemPorIndice (x:xs) i)] ++ cursadasVencidas (x:xs) (i+1)
                          | otherwise = cursadasVencidas (x:xs) (i+1)
                          | (sndTrupla x == 2021) && (third x == 1) = [fstTrupla (accederAElemPorIndice (x:xs) i)] ++ cursadasVencidas (x:xs) (i+1)
                          | otherwise = cursadasVencidas (x:xs) (i+1)