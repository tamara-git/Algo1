--ejercicio 2 del Parcial 

diferencia :: [Integer] -> [Integer]
diferencia [] = []
diferencia [x] = []
diferencia (x:y:xs) = [x-y] ++ diferencia (y:xs)

listaConSignoCambiado :: [Integer] -> [Integer]
listaConSignoCambiado [] = []
listaConSignoCambiado [x] = [-x]
listaConSignoCambiado (x:xs) = [(-1)*x] ++ listaConSignoCambiado xs

esMontaniaRusaAux :: [Integer] -> Bool
esMontaniaRusaAux [] = True
esMontaniaRusaAux [x] | x > 0 = True  
                      | otherwise = False  
esMontaniaRusaAux (x:y:xs) | (x > 0) && (y<0) = esMontaniaRusaAux xs 
                           | otherwise = False

esMontaniaRusa :: [Integer] -> Bool
esMontaniaRusa [] = False 
esMontaniaRusa [x] | x > 0 = esMontaniaRusaAux [x]
                   | x < 0 = esMontaniaRusa (listaConSignoCambiado [x])
esMontaniaRusa (x:xs) | head (diferencia (x:xs)) > 0 = esMontaniaRusaAux (diferencia(x:xs))
                      | head (diferencia (x:xs)) < 0 = esMontaniaRusaAux (listaConSignoCambiado (diferencia(x:xs)))
                      | otherwise = False


--Ejercicio 4 del parcial

pertenece :: Integer -> [Integer] -> Bool
pertenece elemento [] = False 
pertenece elemento [x] | elemento == x = True
                       | otherwise = False 
pertenece elemento (x:xs) | elemento == x = True 
                          | otherwise = pertenece elemento xs

                        
iesimaFila :: [[Integer]] -> Integer -> Integer
iesimaFila [] elemento = 0
iesimaFila [x] elemento | pertenece elemento x = 1
                        | otherwise = 0
iesimaFila (x:xs) elemento | pertenece elemento x = 1 
                         | otherwise = 1 + iesimaFila xs elemento

maximo :: [Integer] -> Integer
maximo [x] = x 
maximo (x:xs) | x >= maximo xs = x 
              | otherwise = maximo xs 

maximoEnMatriz :: [[Integer]] -> Integer
maximoEnMatriz [x] = maximo x 
maximoEnMatriz (x:xs) | maximo x >= maximoEnMatriz xs = maximo x
                      | otherwise = maximoEnMatriz xs

filaDelMaximo :: [[Integer]] -> Integer
filaDelMaximo [] = 0
filaDelMaximo [x] = 1 
filaDelMaximo (x:xs)  | maximo x >= maximoEnMatriz xs = iesimaFila (x:xs) (maximo x) 
                      | otherwise = iesimaFila (x:xs) (maximoEnMatriz xs)