{-Dadas dos tuplas de RxR, decide si cada coordenada de la primera tupla es menor a la coordenada 
correspondiente de la segunda tupla-}
type Punto2D = (Float,Float)
esParMenor :: Punto2D -> Punto2D -> Bool
esParMenor (a,b) (c,d) | (a<c) && (b<d) = True
                       | otherwise = False
