import unittest

from escape_en_solitario import escape_en_solitario

class Test_escape_en_solitario(unittest.TestCase):
    def test_un_solo_solitario(self):
        amigos_por_salas: list[list[int]] =  [[0, 0, 0, 1],
                                              [0, 0, 3, 0],
                                              [40,50,1, 0]]
        res: list[int] = [1]
        self.assertEqual(escape_en_solitario(amigos_por_salas), res )

    def test_tres_solitarios(self):
        amigos_por_salas: list[list[int]] =  [[0, 0, 0, 1],
                                              [0, 0, 3, 0],
                                              [40,50,1, 0],
                                              [0,0, 60, 0],
                                              [0,0, 61, 0]
                                              ]
        res: list[int] = [1]
        self.assertEqual(escape_en_solitario(amigos_por_salas), res )


if __name__ == "__main__":
    unittest.main(verbosity=2)
