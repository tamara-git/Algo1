{-Ejercicio 8. En este ejercicio vamos a trabajar con matrices.
Vamos a representar una matriz como una secuencia de secuencias. Si m es nuestra secuencia de secuencias que representa
una matriz: La secuencia i-´esima de m representa la i-´esima fila de la matriz, y el elemento j-´esimo dentro de la secuencia
i-´esima representa el elemento en la fila i, columna j de la matriz.

Usando esta representaci´on, definir las siguientes funciones sobre matrices:
1. sumaTotal :: [[Integer]] -> Integer seg´un la siguiente especificaci´on:
problema sumaTotal (m: seq⟨seq⟨Z⟩⟩) : Z {
requiere: { |m| > 0 }
requiere: { |m[0]| > 0 }
requiere: { Todos los elementos de la secuencia m tienen la misma longitud }
asegura: { resultado =
P|m|−1
i=0
P|m[i]|−1
j=0 m[i][j] }
}
-}

sumaEnFilas :: [Integer] -> Integer
sumaEnFilas [] = 0
sumaEnFilas [x] = x
sumaEnFilas (x:xs) = x + sumaEnFilas xs

sumaTotal :: [[Integer]] -> Integer
sumaTotal [] = 0
sumaTotal [y] = sumaEnFilas y 
sumaTotal (y:ys) = sumaEnFilas y + sumaTotal ys

{-2. cantidadDeApariciones :: Integer -> [[Integer]] -> Integer según la siguiente especificación:
problema cantidadDeApariciones (e: Z, m: seq⟨seq⟨Z⟩⟩) : Z {
requiere: { |m| > 0 }
requiere: { |m[0]| > 0 }
requiere: { Todos los elementos de la secuencia m tienen la misma longitud }
asegura: { resultado =
P|m|−1
i=0
P|m[i]|−1
j=0 1 si m[i][j] es igual a e, 0 si no }
}-}

cantidadDeAparicionesEnFila :: Integer -> [Integer] -> Integer
cantidadDeAparicionesEnFila e [] = 0
cantidadDeAparicionesEnFila e [x] | e == x = 1 
                                  | otherwise = 0
cantidadDeAparicionesEnFila e (x:xs) | e == x = 1 + cantidadDeAparicionesEnFila e xs 
                                     | otherwise = 0 + cantidadDeAparicionesEnFila e xs

cantidadDeApariciones :: Integer -> [[Integer]] -> Integer
cantidadDeApariciones e [] = 0
cantidadDeApariciones e [x] = cantidadDeAparicionesEnFila e x
cantidadDeApariciones e (x:xs) = cantidadDeAparicionesEnFila e x + cantidadDeApariciones e xs

{-3. contarPalabras :: String ->[[String]] ->Int seg´un la siguiente especificaci´on:
problema contarPalabras (p: String, m: seq⟨seq⟨String⟩⟩) : Z {
requiere: { |m| > 0 }
requiere: { |m[0]| > 0 }
requiere: { Todos los elementos de la secuencia m tienen la misma longitud }
asegura: { El resultado es la cantidad de veces que p aparece exactamente igual en los elementos de m }
}-}

contarPalabrasPorFila :: String -> [String] -> Int
contarPalabrasPorFila p [] = 0
contarPalabrasPorFila p [x] | p == x = 1
                            | otherwise = 0
contarPalabrasPorFila p (x:xs) | p == x = 1 + contarPalabrasPorFila p xs 
                               | otherwise = 0 + contarPalabrasPorFila p xs 


contarPalabras :: String -> [[String]] -> Int 
contarPalabras p [] = 0
contarPalabras p [x] = contarPalabrasPorFila p x
contarPalabras p (x:xs) = contarPalabrasPorFila p x + contarPalabras p xs 

{-4. cantidadDeApariciones2 :: (Eq a) => a -> [[a]] -> Integer tal que pueda usarlo para resolver los dos ejercicios anteriores.-}

cantidadDeAparicionesPorFila2 :: (Eq a) => a -> [a] -> Integer
cantidadDeAparicionesPorFila2 p [] = 0
cantidadDeAparicionesPorFila2 p [x] | p == x = 1 
                                    | otherwise = 0
cantidadDeAparicionesPorFila2 p (x:xs) | p == x = 1 + cantidadDeAparicionesPorFila2 p xs 
                                       | otherwise = 0 + cantidadDeAparicionesPorFila2 p xs 

cantidadDeApariciones2 :: (Eq a) => a -> [[a]] -> Integer
cantidadDeApariciones2 p [] = 0 
cantidadDeApariciones2 p [x] = cantidadDeAparicionesPorFila2 p x 
cantidadDeApariciones2 p (x:xs) = cantidadDeAparicionesPorFila2 p x + cantidadDeApariciones2 p xs  

{-5. multiplicarPorEscalar :: Integer -> [[Integer]] -> [[Integer]] seg´un la siguiente especificaci´on:
problema multiplicarPorEscalar (lambda: Z, m: seq⟨seq⟨Z⟩⟩) : seq⟨seq⟨Z⟩⟩ {
requiere: { |m| > 0 }
requiere: { |m[0]| > 0 }
requiere: { Todos los elementos de la secuencia m tienen la misma longitud }
asegura: { |resultado| = m }
asegura: { Para todo 0 ≤ i < |m|, |resultado[i]| = |m[i]| }
asegura: { Para toda posici´on v´alida i, j de m, resultado[i][j] = lambda × m[i][j]}
}-}

multiplicarPorEscalarEnFila :: Integer -> [Integer] -> [Integer]
multiplicarPorEscalarEnFila escalar [] = []
multiplicarPorEscalarEnFila escalar [x] = [escalar*x]
multiplicarPorEscalarEnFila escalar (x:xs) = [escalar*x] ++ multiplicarPorEscalarEnFila escalar xs
 
multiplicarPorEscalar :: Integer -> [[Integer]] -> [[Integer]]
multiplicarPorEscalar e [] = []
multiplicarPorEscalar e [x] = [multiplicarPorEscalarEnFila e x ]
multiplicarPorEscalar e (x:xs) = [multiplicarPorEscalarEnFila e x] ++ multiplicarPorEscalar e xs

{-6. concatenarFilas :: [[String]] ->[String] seg´un la siguiente especificaci´on:
problema concatenarFilas (m: seq⟨seq⟨String⟩⟩) : seq⟨String⟩ {
requiere: { |m| > 0 }
requiere: { |m[0]| > 0 }
requiere: { Todos los elementos de la secuencia m tienen la misma longitud }
asegura: { |resultado| = |m| }
asegura: { Para todo 0 ≤ i < |m|, resultado[i] = concatenaci´on de todos los strings en m[i] }
}-}


concatenarSecuencia :: [String] -> String
concatenarSecuencia [] = []
concatenarSecuencia [x] = x
concatenarSecuencia (x:xs) = x ++ concatenarSecuencia xs

concatenarFilas :: [[String]] -> [String]
concatenarFilas [] = [concatenarSecuencia []]
concatenarFilas [x] = [concatenarSecuencia x]
concatenarFilas (x:xs) = [concatenarSecuencia x] ++ concatenarFilas xs