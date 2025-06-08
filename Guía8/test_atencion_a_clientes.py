import unittest

from atencion_a_clientes import atencion_a_clientes, Cola,

class Test_atencion_a_clientes(unittest.TestCase):
    def con_una_prioridad(self):
        cola: Cola[tuple[str,int,bool,bool]] = Cola()
        cola.put(("Pablo",47344554,False,True))
        cola.put(("Brunilda", 94256891, False, True))
        cola.put(("Kiara", 10245697, True, False))
        cola.put(("Tamara", 46683766, False, False))

        cola_ordenada: Cola[tuple[str,int,bool,bool]] = Cola()
        cola_ordenada.put(("Kiara", 10245697, True, False))
        cola_ordenada.put(("Pablo", 47344554,False,True))
        cola_ordenada.put(("Brunilda", 94256891, False, True))
        cola_ordenada.put(("Tamara", 46683766, False, False))

        self.assertTrue(son_colas_iguales(atencion_a_clientes(cola), cola_ordenada))


if __name__ == "__main__":
    unittest.main(verbosity=2)