module TestMaximo where

import Test.HUnit
import maximo

-- Casos de Testo
run = runTestTT testsMaximo

testsMaximo = test [
  "Tablero con una fila" ~: (maximo ([[1,2,6,4,3]])) ~?= 6,
  "Tablero con dos filas" ~: (maximo([[4,3,2,1],[10,9,8,7]])) ~?= 10,
 ]


