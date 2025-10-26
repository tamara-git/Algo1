import unittest
from mi_parcial import reordenar_cola_priorizando_vips_mostrar, nivel_de_ocupacion
from queue import Queue as Cola

class test_reordenar(unittest.TestCase):
    def test_ejemplo(self):
        cola: Cola[tuple[str,str]] = Cola()
        cola.put(("Ana","comun"))
        cola.put(("Juli","vip"))
        cola.put(("Fede","vip"))
        res: list[str] = ["Juli","Fede","Ana"]
        self.assertEqual(reordenar_cola_priorizando_vips_mostrar(cola),res)

    def test_todos_comunes(self):
        cola: Cola[tuple[str,str]] = Cola()
        cola.put(("Ana","comun"))
        cola.put(("Juli","comun"))
        cola.put(("Fede","comun"))
        res: list[str] = ["Ana","Juli","Fede"]
        self.assertEqual(reordenar_cola_priorizando_vips_mostrar(cola),res)

    def test_dos_comunes_un_vips(self):
        cola: Cola[tuple[str,str]] = Cola()
        cola.put(("Ana","comun"))
        cola.put(("Juli","comun"))
        cola.put(("Fede","vip"))
        res: list[str] = ["Fede","Ana","Juli"]
        self.assertEqual(reordenar_cola_priorizando_vips_mostrar(cola),res)

class test_nivel_de_ocupacion(unittest.TestCase):
    def test_ejemplo(self):
        camas_por_piso: list[list[bool]] =  [[False, False, False], [False, False, False],[True, True, True]] 
        esperado: list[float] = [0.0, 0.0, 1.0]
        self.assertEqual(nivel_de_ocupacion(camas_por_piso),esperado)


    def test_ejemplo_2(self):
        camas_por_piso: list[list[bool]] = [[True, False, True], [False, False, True],[True, True, True]]
        esperado: list[float] = [2/3, 1/3, 1.0]
        self.assertEqual(nivel_de_ocupacion(camas_por_piso),esperado)
if __name__ == '__main__':
    unittest.main(verbosity=2)