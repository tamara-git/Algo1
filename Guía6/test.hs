module Tests where
import Test.HUnit
import TestFibo 

testFibonacci = test [
"Positivo" ~: fib 5 ~?= 5
    ] 