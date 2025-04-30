{-capicua :: (Eq t) => [t] -> Bool seg´un la siguiente especificaci´on:
problema capicua (s: seq⟨T⟩) : B {
requiere: { T rue }
asegura: { (resultado = true) ↔ (s = reverso(s)) }
}
Por ejemplo capicua [´a’,’c’, ’b’, ’b’, ’c’, ´a’] es true, capicua [´a’, ’c’, ’b’, ’d’, ´a’] es false.
-}

reverso :: [t] -> [t]
reverso [] = []
reverso [x] = [x]
reverso (x:xs) = reverso (xs) ++ [x]

capicua ::  (Eq t) => [t] -> Bool
capicua [] = True
capicua (x:xs) | (x:xs) == reverso (x:xs) = True
               | otherwise = False