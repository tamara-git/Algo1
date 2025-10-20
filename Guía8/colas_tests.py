import unittest
from queue import Queue as Cola
from colas import jugar_carton_de_bingo

class test_jugar_carton_de_bingo(unittest.TestCase):
    def test_minima_jugada(self):
        bolillero: Cola = Cola()
        bolillero.put(45)
        bolillero.put(1)
        bolillero.put(5)
        bolillero.put(2)
        bolillero.put(15)
        bolillero.put(23)
        bolillero.put(32)
        bolillero.put(21)
        bolillero.put(20)
        bolillero.put(10)
        bolillero.put(9)
        bolillero.put(90)
        bolillero.put(30)
        bolillero.put(50)
        bolillero.put(78)
        carton: list[int] = [45,1,5,2,15,23,32,21,20,10,9,90]
        res: int = 12
        self.assertEqual(jugar_carton_de_bingo(carton, bolillero), res)

    def test_15_jugadas(self):
        bolillero: Cola = Cola()
        bolillero.put(78)
        bolillero.put(50)
        bolillero.put(5)
        bolillero.put(2)
        bolillero.put(15)
        bolillero.put(23)
        bolillero.put(32)
        bolillero.put(21)
        bolillero.put(20)
        bolillero.put(10)
        bolillero.put(9)
        bolillero.put(90)
        bolillero.put(30)
        bolillero.put(1)
        bolillero.put(45)
        carton: list[int] = [45,1,5,2,15,23,32,21,20,10,9,90]
        res: int = 15
        self.assertEqual(jugar_carton_de_bingo(carton, bolillero), res)






if __name__ == '__main__':
    unittest.main(verbosity=2)