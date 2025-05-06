{-problema hayQueCodificar (c: Char, mapeo: seq⟨Char x Char⟩ ) : Bool {
  requiere: {No hay elementos repetidos entre las primeras componentes de mapeo}
  requiere: {No hay elementos repetidos entre las segundas componentes de mapeo}
  asegura: {res = true <=> c es igual a la primera componente de alguna tupla de mapeo}
}
-}

hayQueCodificar :: Char -> [(Char,Char)] -> Bool
hayQueCodificar y [] = True
hayQueCodificar y (x:[]) | y == fst x = True
                         | otherwise = False
hayQueCodificar y (x:xs) | y == fst x = True 
                         | otherwise = hayQueCodificar y (xs) 

{-problema cuantasVecesHayQueCodificar (c: Char, frase: seq⟨Char⟩, mapeo: seq⟨Char x Char⟩ ) : Z {
  requiere: {No hay elementos repetidos entre las primeras componentes de mapeo}
  requiere: {No hay elementos repetidos entre las segundas componentes de mapeo}
  requiere: {|frase| > 0 }
  requiere: {c pertenece a frase}
  asegura: {(res = 0 y hayQueCodificar (c, mapeo) = false) o (res = cantidad de veces que c aparece en frase y hayQueCodificar (c, mapeo) = true)}
}
-}

vecesQueApareceEnFrase :: Char -> [Char] -> Int
vecesQueApareceEnFrase c [] = 0
vecesQueApareceEnFrase c (x:xs) | c /= x = vecesQueApareceEnFrase c xs
                                 | otherwise = 1 + vecesQueApareceEnFrase c xs

cuantasVecesHayQueCodificar :: Char -> [Char] -> [(Char,Char)] -> Int 
cuantasVecesHayQueCodificar c frase mapeo | hayQueCodificar c mapeo == False = 0
                                          | otherwise = vecesQueApareceEnFrase c frase 

{-problema laQueMasHayQueCodificar (frase: seq⟨Char⟩, mapeo: seq⟨Char x Char⟩ ) : Char {
  requiere: {No hay elementos repetidos entre las primeras componentes de mapeo}
  requiere: {No hay elementos repetidos entre las segundas componentes de mapeo}
  requiere: {|frase| > 0 }
  requiere: {Existe al menos un c que pertenece a frase y hayQueCodificar(c, mapeo)=true}
  asegura: {res = c donde c es el caracter tal que cuantasVecesHayQueCodificar(c, frase, mapeo) es mayor a cualquier otro caracter perteneciente a frase}
  asegura: {Si existen más de un caracter c que cumple la condición anterior, devuelve el que aparece primero en frase }-}
 
maximoACodificar :: [Char] -> [(Char,Char)] -> Char
maximoACodificar (x:[]) mapeo = x 
maximoACodificar (x:xs) mapeo | cuantasVecesHayQueCodificar x (x:xs) mapeo >= cuantasVecesHayQueCodificar (maximoACodificar (xs) mapeo) (x:xs) mapeo = x
                              | otherwise = maximoACodificar (xs) mapeo

laQueMasHayQueCodificar :: [Char] -> [(Char,Char)] -> Char
laQueMasHayQueCodificar frase mapeo = maximoACodificar frase mapeo

{-problema codificarFrase (frase: seq⟨Char⟩, mapeo: seq⟨Char x Char⟩ ) : seq ⟨Char⟩ {
  requiere: {No hay elementos repetidos entre las primeras componentes de mapeo}
  requiere: {No hay elementos repetidos entre las segundas componentes de mapeo}
  requiere: {|frase| > 0 }
  asegura: {|res| = |frase|}
  asegura: { Para todo 0 <= i < |frase| si hayQueCodificar(frase[i], mapeo) = true
   entonces res[i]= (mapeo[j])1, para un j tal que 0 <= j < |mapeo| y mapeo[j])0 = frase[i] }
  asegura: { Para todo 0 <= i < |frase| si hayQueCodificar(frase[i], mapeo) = false entonces res[i]= frase[i]}
} -}

-- ejemplo: de "hola" quiero ver si cada caracter es codificable o no  
--quiero correr la lista caracter por caracter

codificarUnCaracter :: Char -> [(Char,Char)] -> Char
codificarUnCaracter y (x:[]) | (hayQueCodificar y (x:[])== True) && (y == fst x ) = snd x
codificarUnCaracter y (x:xs) | (hayQueCodificar y (x:xs) == True) && (y == fst x) = snd x
                             | hayQueCodificar y (x:xs) == False = y 
                             | otherwise = codificarUnCaracter y (xs)

codificarCaracteres :: [Char] -> [(Char,Char)] -> [Char]
codificarCaracteres (x:[]) (y:ys) | hayQueCodificar x (y:ys) == True = [codificarUnCaracter x (y:ys)]
codificarCaracteres (x:xs) (y:ys) | hayQueCodificar x (y:ys) == False = x:codificarCaracteres (xs) (y:ys)
                                  | otherwise = codificarUnCaracter x (y:ys):codificarCaracteres (xs) (y:ys)

--codificarFrase :: [Char] -> [(Char,Char)] -> [Char]
--codificarFrase frase mapeo | hayQueCodificar c mapeo == True = codificarCaracteres
--                           | otherwise = 
