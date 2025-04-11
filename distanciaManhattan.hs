{-problema distanciaManhattan (p: RxRxR, q: RxRxR) : R {
   requiere: {True}
   asegura: {res = Sumatoria de i=0 a 2 |pi - qi|}
} -}

type Punto3D = (Float, Float, Float)

absoluto :: Punto3D -> Punto3D
absoluto x y  | (x < 0) == -(x-y)
              | (y < 0) == -(x-y)
              | otherwise = x-y
                 
distanciaManhattan :: Punto3D -> Punto3D -> Float
distanciaManhattan (a,b,c) (d,e,f) = absoluto a d + absoluto b e + absoluto c f