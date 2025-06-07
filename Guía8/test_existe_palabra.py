import unittest

from existe_palabra import existe_palabra

class Test_existe_palabra(unittest.TestCase):
    def test_una_linea(self):
        self.assertTrue(existe_palabra("linea.txt", "verano"))
        self.assertFalse(existe_palabra("linea.txt", "invierno"))

if __name__ == "__main__":
    unittest.main(verbosity=2)
