menorDivisorDesde :: Integer -> Integer -> Integer
menorDivisorDesde n d | (n >= 0) && (d <= n ) && (mod n d == 0) = d
                      | (n >= 0) && (d <= n ) && (mod n d /= 0) = 0 + menorDivisorDesde n (d+1)
                      | (n < 0) && (d <= -1 ) && (mod n d == 0) = d
                      | (n < 0) && (d <= -1 ) && (mod n d /= 0) = 0 + menorDivisorDesde n (d+1)
                      | otherwise = 0


menorDivisor :: Integer -> Integer
menorDivisor n | n >= 0 = menorDivisorDesde n 2 
               | otherwise = menorDivisorDesde n (n+1)

esPrimo :: Integer -> Bool
esPrimo n | (n >= 0) && (menorDivisor n == n) = True
          | (n < 0) && (menorDivisor n == -1) = True
          | otherwise = False 

listaDePrimos :: [Integer] -> [Integer]
listaDePrimos [] = []
listaDePrimos [x] | esPrimo x == True = [x]
                  | otherwise = []
listaDePrimos (x:xs) | esPrimo x == True = x:listaDePrimos xs
                     | otherwise = listaDePrimos xs

menorEnSecuencia :: [Integer] -> Integer
menorEnSecuencia [x] = x 
menorEnSecuencia (x:xs) | x <= menorEnSecuencia xs = x
                        | otherwise = menorEnSecuencia xs


menorPrimo :: [Integer] -> Integer
menorPrimo [x] = x
menorPrimo (x:xs) = menorEnSecuencia(listaDePrimos(x:xs)) 

--Ejercicio 1
fstTrupla :: (String, Integer, [(Integer,Integer)]) -> String
fstTrupla (a,b,c) = a 

sndTrupla :: (String, Integer, [(Integer,Integer)]) -> Integer
sndTrupla (a,b,c) = b 

thrTrupla :: (String, Integer, [(Integer,Integer)]) -> [(Integer,Integer)]
thrTrupla (a,b,c) = c 


productoDeTuplas :: (Integer,Integer) -> Integer 
productoDeTuplas (a,b) = a*b 

productoEnLista :: [(Integer,Integer)] -> [Integer] 
productoEnLista [] = []
productoEnLista [x] = [productoDeTuplas x] 
productoEnLista (x:xs) = [productoDeTuplas x] ++ productoEnLista xs 

esIgualAUnElemento :: Integer -> [Integer] -> Bool
esIgualAUnElemento e [] = False 
esIgualAUnElemento e [x] | e == x = True 
esIgualAUnElemento e (x:xs) | e == x = True 
                            | otherwise = esIgualAUnElemento e xs

productosSinInteres :: [(String, Integer, [(Integer,Integer)])] -> [String]
productosSinInteres [] = []
productosSinInteres [x] | esIgualAUnElemento (sndTrupla x) (productoEnLista (thrTrupla x)) == True = [fstTrupla x]
                        | otherwise = []
productosSinInteres (x:xs) | esIgualAUnElemento (sndTrupla x) (productoEnLista (thrTrupla x)) == True = [fstTrupla x] ++ productosSinInteres xs
                           | otherwise = productosSinInteres xs 