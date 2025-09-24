{-Implementar la función sonCoprimos que dados dos números naturales indica si no tienen algún divisor
en común mayor estricto que 1. -}

divisoresDe :: Integer -> Integer -> [Integer]
divisoresDe n desde | (desde <= n) && mod n desde /= 0 = [] ++ divisoresDe n (desde + 1)
                    | (desde <= n) && mod n desde == 0 = [desde] ++ divisoresDe n (desde + 1)
                    | otherwise = []

hayDivisorComun :: [Integer] -> [Integer] -> Bool
hayDivisorComun [] [] = True
hayDivisorComun [x] [] = False
hayDivisorComun [] [y] = False
hayDivisorComun [x] [y] | x == y = True
                        | otherwise = False 
hayDivisorComun (x:xs) [y] | x == y = True
                           | otherwise = hayDivisorComun xs [y]
hayDivisorComun [x] (y:ys) | x == y = True 
                           | otherwise = hayDivisorComun [x] ys
hayDivisorComun (x:xs) (y:ys) | x == y = True
                              | x /= y = hayDivisorComun [x] ys 
                              | otherwise = hayDivisorComun xs (y:ys)

sonCoprimos :: Integer -> Integer -> Bool 
sonCoprimos n m | hayDivisorComun (divisoresDe n 2) (divisoresDe m 2) == False = True
                | otherwise = False