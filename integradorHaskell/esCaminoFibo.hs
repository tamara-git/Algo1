{-Ejercicio 8. Implementar la funci´on esCaminoFibo :: [Int] ->Int ->Bool
problema esCaminoFibo (s:seq⟨Z⟩, i : Z) : Bool {
asegura: {res = true ⇔ los valores de s son la sucesi´on de Fibonacci inicializada con el n´umero pasado como
par´ametro i}
}
La sucesión de Fibonacci est´a definida con la siguiente funci´on recursiva:
f(0) = 0     0,1,1,2,3,5  ,8,
f(1) = 1
f(n) = f(n-1) + f(n-2) con n>1
En el ejemplo del tablero y del camino (verde claro) que figuran m´as arriba tenemos que esCaminoFibo [1,1,2,3,5] 1
reduce a True.
esCaminoFibo (valoresDeCamino tablero [(3,2), (4, 2), (4,3)]) 3, siendo tablero el del ejemplo, tambi´en reduce a
True.
-}

longitud :: [Int] -> Int
longitud [x] = 1
longitud (x:xs) = 1 + longitud xs


fibonacci :: Int -> Int
fibonacci 0 = 0
fibonacci 1 = 1
fibonacci n = fibonacci (n-1) + fibonacci (n-2)


fibonacciDesdeHasta :: Int -> Int -> [Int]
fibonacciDesdeHasta i n | i <= n = [fibonacci i] ++ fibonacciDesdeHasta (i+1) n
                        | otherwise = []

esCaminoFibo :: [Int] -> Int -> Bool
esCaminoFibo [x] i | [x] == fibonacciDesdeHasta i (longitud [x]) = True
                   | otherwise = False
esCaminoFibo (x:xs) i | (x:xs) == fibonacciDesdeHasta i ((i-1) + longitud (x:xs)) = True
                      | otherwise = False