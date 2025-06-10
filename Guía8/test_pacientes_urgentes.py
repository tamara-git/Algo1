import unittest 

from pacientes_urgentes import pacientes_urgentes, Cola

class Test_pacientes_urgentes(unittest.TestCase):
    def test_dos_pac_menor_a_cuatro(self):
        c: Cola[tuple[int,str,str]] = Cola()
        c.put((3,"Martín", "Cardiólogo"))
        c.put((2,"Martín", "Cardiólogo"))

        self.assertEqual(pacientes_urgentes(c), 2)

    def test_pacientes_mayor_igual_a_cuatro(self):
        c: Cola[tuple[int,str,str]] = Cola()
        c.put((4,"Martín", "Cardiólogo"))
        c.put((9,"Martín", "Cardiólogo"))

        self.assertEqual(pacientes_urgentes(c), 0)

    
if __name__ == "__main__":
    unittest.main(verbosity=2)
