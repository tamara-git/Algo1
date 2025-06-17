import unittest

from cuantos_sufijos_son_palindromos import cuantos_sufijos_son_palindromos

class Test_cuantos_sufijos_son_palindromos(unittest.TestCase):
    def test_un_sufijo(self):
        texto: str = "loco"

        self.assertEqual(cuantos_sufijos_son_palindromos(texto), 1)
