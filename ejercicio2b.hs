absoluto :: Integer -> Integer
absoluto x  | x < 0 = -x
            | x >= 0 = x

maximoAbsoluto :: Integer -> Integer -> Integer
maximoAbsoluto x y | absoluto x >= absoluto y = absoluto x
                   | otherwise absoluto y
                