import unittest 
from integrador import *

class Test_empleado_del_mes(unittest.TestCase):
    def test_ejemplo(self):
        horas: dict[int,list[int]] = {123: [8,4,6,3], 456: [1,2,3,4], 789: [4,5,6,7], 101112: [8,9,10]}
        res: list[int] = [101112]
        
        self.assertEqual(empleado_del_mes(horas), res)
        
    def test_ejemplo_2(self):
        horas: dict[int,list[int]] = {123: [8,4,6,3], 456: [1,2,3,4], 789: [10,10,7], 101112: [8,9,10]}
        res: list[int] = [789,101112]
        
        self.assertEqual(empleado_del_mes(horas), res)        

class Test_alarma_epidemiologica(unittest.TestCase):
    def test_una_infeccion(self):
        registros: list[tuple[int,str]] = [(123,"VIH"),(456,"Gripe"),(567, "dolor cabeza"), (789, "resfrío")]
        infecciosas: list[str] = ["VIH"]
        res: dict[str,float] = {}
        umbral: float = 0.5
        self.assertEqual(alarma_epidemiologica(registros,infecciosas,umbral), res)
        
    def test_tres_infecciones(self):
        registros: list[tuple[int,str]] = [(456,"Hepatitis B"),(567, "Hepatitis B"),(789, "Hepatitis B"), (765,"Hepatitis B"),(657, "Hepatitis B")]
        infecciosas: list[str] = ["VIH", "Hepatitis B"]
        res: dict[str,float] = {}
        umbral: float = 0.5
        
    def test_no_supera_el_umbral(self):
        registros: list[tuple[int,str]] = [(123,"VIH"),(456,"Gripe"),(1,"Gripe"),(4,"Gripe"),(6,"Gripe"),(567, "dolor cabeza"),(789, "resfrío"),(9, "resfrío"),(15, "resfrío"), (765,"Hepatitis B"),(657, "Hepatitis B")]
        infecciosas: list[int] = ["VIH", "Hepatitis B", "Hepatitis C"]
        res: dict[str,float] = {"Hepatitis B": 2/11}
        umbral: float = 0.1
        
        self.assertEqual(alarma_epidemiologica(registros,infecciosas,umbral), res)
        
if __name__ == '__main__':
    unittest.main(verbosity=2)