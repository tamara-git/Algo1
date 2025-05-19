import unittest

from pertenece import pertenece

class Test_pertenece(unittest.TestCase):

    def test_pertenece_lista_vacia(self):
        self.assertFalse(pertenece())

