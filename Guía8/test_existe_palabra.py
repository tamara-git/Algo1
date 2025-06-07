import unittest

from existe_palabra import existe_palabra, TextIO

class Test_existe_palabra(unittest.Testcase):
    def test_una_linea(self):
        archivo: TextIO = open("linea.txt", "r", encoding = "utf-8")
        
        
        self.assertTrue(existe_palabra("linea.txt", "verano"))
        self.assertFalse(existe_palabra("linea.txt", "invierno"))



