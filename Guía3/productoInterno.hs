{-Calcula el producto interno entre dos tuplas de RxR-}
type Punto2D = (Float, Float)
productoInterno :: Punto2D -> Punto2D -> Float
productoInterno (a,b) (c,d) = ((a*c) + (b*d))