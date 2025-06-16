import unittest

from tiempo_mas_rapido import tiempo_mas_rapido

class Test_tiempo_mas_rapido(unittest.TestCase):
    def test_unico_tiempo_rapido(self):
        tiempos_salas: list[int] = [4,6,2,7,9,3]
        res: int = 4

        self.assertEqual(tiempo_mas_rapido(tiempos_salas), res)

    def test_dos_tiempos_rapidos(self):
        tiempos_salas: list[int] = [4,6,2,7,9,3,24,6,8,13,24]
        res: int = 6

        self.assertEqual(tiempo_mas_rapido(tiempos_salas), res)

if __name__ == "__main__":
    unittest.main(verbosity=2)