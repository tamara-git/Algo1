
--Ejercicio De clase
multiplicarUnaSolaFila :: [Integer] -> Integer
multiplicarUnaSolaFila [x] = x 
multiplicarUnaSolaFila (x:xs) = x * multiplicarUnaSolaFila xs


multiplicarFilas :: [[Integer]] -> [Integer]
multiplicarFilas [] = []
multiplicarFilas (x:xs) = ((multiplicarUnaSolaFila x) : multiplicarFilas xs)