import unittest

from un_responsable_por_turno import un_responsable_por_turno

class Test_responsable_por_turno(unittest.TestCase):
    def test_un_responsable(self):
        grilla_horaria: list[list[int]] = [["a","a","a","a","a","a","a"],
                                           ["a","a","a","a","a","a","a"],
                                           ["a","a","a","a","a","a","a"],
                                           ["a","a","a","a","a","a","a"],
                                           ["a","a","a","a","a","a","a"],
                                           ["a","a","a","a","a","a","a"],
                                           ["a","a","a","a","a","a","a"],
                                           ["a","a","a","a","a","a","a"]]
        self.assertTrue(un_responsable_por_turno(grilla_horaria), [(True,True),(True,True),(True,True),(True,True),(True,True),(True,True),(True,True)])


if __name__ == "__main__":
    unittest.main(verbosity=2)