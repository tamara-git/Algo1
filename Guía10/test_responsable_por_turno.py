import unittest

from un_responsable_por_turno import un_responsable_por_turno

class Test_responsable_por_turno(unittest.TestCase):
    def test_un_responsable(self):
        grilla_horaria: list[list[str]] = [["a","a","a","a","a","a","a"],
                                           ["a","a","a","a","a","a","a"],
                                           ["a","a","a","a","a","a","a"],
                                           ["a","a","a","a","a","a","a"],
                                           ["a","a","a","a","a","a","a"],
                                           ["a","a","a","a","a","a","a"],
                                           ["a","a","a","a","a","a","a"],
                                           ["a","a","a","a","a","a","a"]]
        self.assertEqual(un_responsable_por_turno(grilla_horaria), [(True,True),(True,True),(True,True),(True,True),(True,True),(True,True),(True,True)])

    def test_2_responsables(self):
        grilla_horaria: list[list[str]] = [["a","b","c","d","e","f","g"],
                                           ["a","b","c","d","e","f","g"],
                                           ["a","b","c","d","e","f","g"],
                                           ["a","b","c","d","e","f","g"],
                                           ["n","x","h","m","z","u","y"],
                                           ["n","x","h","m","z","u","y"],
                                           ["n","x","h","m","z","u","y"],
                                           ["n","x","h","m","z","u","y"]]
        
        self.assertEqual(un_responsable_por_turno(grilla_horaria), [(True,True),(True,True),(True,True),(True,True),(True,True),(True,True),(True,True)])

if __name__ == "__main__":
    unittest.main(verbosity=2)