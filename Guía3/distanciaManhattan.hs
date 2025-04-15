{-problema distanciaManhattan (p: RxRxR, q: RxRxR) : R {
   requiere: {True}
   asegura: {res = Sumatoria de i=0 a 2 |pi - qi|}
} -}

type Punto3D = (Float, Float, Float)

absoluto :: Float -> Float -> Float
absoluto x y  | x < y = -(x-y)
              | otherwise = x-y

distanciaManhattan :: Punto3D -> Punto3D -> Float
distanciaManhattan (a,b,c) (d,e,f) = absoluto a d + absoluto b e + absoluto c f