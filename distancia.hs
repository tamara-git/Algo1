--Calcula la distancia euclídea entre dos puntos de RxR
type Punto2D = (Float,Float)
distancia_al_cuadrado :: Punto2D -> Float
distancia_al_cuadrado (a,b) (c,d) = (a-c)**2 + (b-d)**2

distancia :: Punto2D -> Float
distancia (a,b) (c,d) = sqrt (distancia_al_cuadrado)