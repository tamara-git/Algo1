{-problema distanciaManhattan (p: RxRxR, q: RxRxR) : R {
   requiere: {True}
   asegura: {res = Sumatoria de i=0 a 2 |pi - qi|}
} -}

type Punto3D = (Float, Float, Float)

absoluto :: Punto3D -> Punto3D
absoluto (a,b,c) (d,e,f) | (a+b+c) - (d+e+f) = (d+e+f) - (a+b+c)
                 
distanciaManhattan :: Punto3D -> Punto3D -> Float
distanciaManhattan (a,b,c) (d,e,f) = absoluto (a,b,c) (d,e,f)