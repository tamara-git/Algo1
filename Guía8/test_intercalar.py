import unittest

from intercalar import intercalar, Cola

class Test_intercalar(unittest.TestCase):
    def cola_corta(self):

        c1: Cola = Cola()
        c1.put(1)
        c1.put(2)
        c1.put(10)

        c2: Cola = Cola()
        c2.put(20)
        c2.put(30)
        c2.put(15)

        res: Cola = Cola()
        res.put(1)
        res.put(20)
        res.put(2)
        res.put(30)
        res.put(10)
        res.put(15)

        self.assertEqual(intercalar(c1,c2),res)

if __name__ == "__main__":
    unittest.main(verbosity=2)