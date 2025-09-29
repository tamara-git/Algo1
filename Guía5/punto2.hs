{-1. pertenece :: (Eq t) => t -> [t] -> Bool según la siguiente especificación:
problema pertenece (e: T, s: seq⟨T⟩) : B {
requiere: { T rue }
asegura: { resultado = true ↔ e ∈ s }
}
-}

pertenece :: (Eq t) => t -> [t] -> Bool 
pertenece e [] = False
pertenece e [x] | e == x = True 
                | otherwise = False 
pertenece e (x:xs) | e == x = True 
                   | otherwise = pertenece e xs

{-2. todosIguales :: (Eq t) => [t] -> Bool, que dada una lista devuelve verdadero sí y solamente sí todos sus elementos son iguales.-}

todosIguales :: (Eq t) => [t] -> Bool 
todosIguales [] = False
todosIguales [x] = True 
todosIguales (x:y:xs) | x == y = todosIguales (y:xs)
                      | otherwise = False


{-3. todosDistintos :: (Eq t) => [t] -> Bool según la siguiente especificación:
problema todosDistintos (s: seq⟨T⟩) : B {
requiere: { True }
asegura: { resultado = False ↔ existen dos posiciones distintas de s con igual valor }
}-}

todosDistintos :: (Eq t) => [t] -> Bool 
todosDistintos [x] = True 
todosDistintos (x:xs) | pertenece x xs == True = False  
                      | otherwise = todosDistintos xs

{-4. hayRepetidos :: (Eq t) => [t] -> Bool seg´un la siguiente especificación:
problema hayRepetidos (s: seq⟨T⟩) : B {
requiere: { True }
asegura: { resultado = true ↔ existen dos posiciones distintas de s con igual valor }
}-}

hayRepetidos :: (Eq t) => [t] -> Bool 
hayRepetidos [] = False 
hayRepetidos [x] = False 
hayRepetidos (x:xs) = not (todosDistintos (x:xs))

{-5.quitar :: (Eq t) => t -> [t] -> [t], que dados un entero x y una lista xs, elimina la primera aparici´on de x en
la lista xs de haberla-}

quitar :: (Eq t) => t -> [t] -> [t]
quitar x [] = []
quitar x [y] | x == y = []
             | otherwise = [y]
quitar x (y:ys) | x == y = ys 
                | otherwise = y:quitar x ys

{-6.quitarTodos :: (Eq t ) => t -> [t] -> [t], que dados un entero x y una lista xs, elimina todas las apariciones
de x en la lista xs (de haberlas). Es decir:
problema quitarTodos (e: T , s: seq⟨T ⟩) : seq⟨T ⟩ {
requiere: { T rue }
asegura: { resultado es igual a s pero sin el elemento e. }
}-}

quitarTodos :: (Eq t ) => t -> [t] -> [t]
quitarTodos x [] = []
quitarTodos x [y] | x == y = []
                  | otherwise = [y]
quitarTodos x (y:ys) | x == y = quitarTodos x ys
                     | otherwise = y:quitarTodos x ys

{-7. eliminarRepetidos :: (Eq t) => [t] -> [t] que deja en la lista una única aparición de cada elemento, eliminando
las repeticiones adicionales.-}

eliminarRepetidos :: (Eq t) => [t] -> [t]
eliminarRepetidos [] = []
eliminarRepetidos [x] = [x]
eliminarRepetidos (x:xs) | pertenece x xs = x:eliminarRepetidos (quitarTodos x xs)
                         | otherwise = x:eliminarRepetidos xs

{-mismosElementos :: (Eq t) => [t] -> [t] -> Bool, que dadas dos listas devuelve verdadero sí y solamente sí
ambas listas contienen los mismos elementos, sin tener en cuenta repeticiones, es decir:
problema mismosElementos (s: seq⟨T⟩, r: seq⟨T⟩) : B {
requiere: { True }
asegura: { resultado = true ↔ todo elemento de s pertenece a r y viceversa}
}
-}

pertenecenTodosElementos :: (Eq t) => [t] -> [t] -> Bool
pertenecenTodosElementos [] [] = True
pertenecenTodosElementos [x] [] = False
pertenecenTodosElementos [x] [y] | x == y = True
                                 | otherwise = False
pertenecenTodosElementos [x] (y:ys) | pertenece x (y:ys) = True 
                                    | otherwise = False
pertenecenTodosElementos (x:xs) (y:ys) | pertenece x (y:ys) == True = pertenecenTodosElementos xs (y:ys)
                                       | otherwise = False

mismosElementos :: (Eq t) => [t] -> [t] -> Bool
mismosElementos [] [] = False
mismosElementos [x] [] = False
mismosElementos [] [y] = False 
mismosElementos [x] [y] | x == y = True 
                        | otherwise = False 
mismosElementos [x] (y:ys) | pertenecenTodosElementos [x] (y:ys) == True && pertenecenTodosElementos (y:ys) [x] == True = True
                           | otherwise = False
mismosElementos (x:xs) (y:ys) | pertenecenTodosElementos (x:xs) (y:ys) == True && pertenecenTodosElementos (y:ys) (x:xs) == True = True 
                              | otherwise = False

{-9. capicua :: (Eq t) => [t] -> Bool seg´un la siguiente especificaci´on:
problema capicua (s: seq⟨T⟩) : B {
requiere: { True }
asegura: { (resultado = true) ↔ (s = reverso(s)) }
}
Por ejemplo capicua [´a’,’c’, ’b’, ’b’, ’c’, ´a’] es true, capicua [´a’, ’c’, ’b’, ’d’, ´a’] es false.-}

reverso :: [t] -> [t]
reverso [] = []
reverso [x] = [x]
reverso (x:xs) = reverso (xs) ++ [x]

capicua :: (Eq t) => [t] -> Bool 
capicua [] = True
capicua [x] = True
capicua (x:xs) | reverso (x:xs) == (x:xs) = True 
               | otherwise = False