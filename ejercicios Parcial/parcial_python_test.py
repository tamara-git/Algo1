import unittest
from queue import Queue as Cola
from parcial_python import cantidad_parejas_que_suman, pasar_por_autoservicio, pasar_por_autoservicio_testeo_len, mantuvieron_residencia

class Test_cantidad_parejas_que_suman(unittest.TestCase):
    def test_ejemplo(self):
        s: list[int] = [1,3,2,5,4,8,3,2]
        n: int = 5
        res: int = 5
        self.assertEqual(cantidad_parejas_que_suman(s,n), res) 

    def test_sin_cantidad(self):
        s: list[int] = [1,3,2,5,4,8]
        n: int = 1
        res: int = 0
        self.assertEqual(cantidad_parejas_que_suman(s,n), res) 

    def test_1_cantidad(self):
        s: list[int] = [1,3,2,5,4,-1]
        n: int = 1
        res: int = 1
        self.assertEqual(cantidad_parejas_que_suman(s,n), res) 

class Test_pasar_por_autoservicio(unittest.TestCase):
    def test_ejemplo(self):
        res: str = "Juan"
        clientes: Cola[tuple[str,str,int]] = Cola()
        clientes.put(("Ana", "tarjeta", 22))
        clientes.put(("Juan", "qr", 13))
        clientes.put( ("Bruno", "tarjeta", 14))
        self.assertEqual(pasar_por_autoservicio(clientes), res)


    def test_verificar_len(self):
        clientes: Cola[tuple[str,str,int]] = Cola()
        clientes.put(("Ana", "tarjeta", 22))
        clientes.put(("Juan", "qr", 13))
        clientes.put( ("Bruno", "tarjeta", 14))
        self.assertEqual(len(pasar_por_autoservicio_testeo_len(clientes)), 2)

    def test_todos_cumplen(self):
        res: str = "Ana"
        clientes: Cola[tuple[str,str,int]] = Cola()
        clientes.put(("Ana", "tarjeta", 10))
        clientes.put(("Juan", "qr", 13))
        clientes.put( ("Bruno", "tarjeta", 14))
        self.assertEqual(pasar_por_autoservicio(clientes), res)

    def test_verificar_len_todos_cumplen(self):
        clientes: Cola[tuple[str,str,int]] = Cola()
        clientes.put(("Ana", "tarjeta", 10))
        clientes.put(("Juan", "qr", 13))
        clientes.put( ("Bruno", "tarjeta", 14))
        self.assertEqual(len(pasar_por_autoservicio_testeo_len(clientes)), 2)

class Test_mantuvieron_residencia(unittest.TestCase):
    def test_mantuvieron_residencia(self):
        censo1: dict[str,str] ={'Juan': 'Merlo', 'Ana': 'Merlo'}
        censo2: dict[str,str] = {'Juan': 'Castelar', 'Ana': 'Merlo'}
        res: dict[str,int] = {'Merlo': 1}
        self.assertEqual(mantuvieron_residencia(censo1,censo2), res)
        
    def test_dos_mantuvieron_residencia_distinta(self):
        censo1: dict[str,str] ={'Juan': 'Castelar', 'Ana': 'Merlo'}
        censo2: dict[str,str] = {'Juan': 'Castelar', 'Ana': 'Merlo'}
        res: dict[str,int] = { 'Castelar': 1,'Merlo': 1}
        self.assertEqual(mantuvieron_residencia(censo1,censo2), res)

    def test_dos_mantuvieron_misma_residencia(self):
        censo1: dict[str,str] ={'Juan': 'Merlo', 'Ana': 'Merlo'}
        censo2: dict[str,str] = {'Juan': 'Merlo', 'Ana': 'Merlo'}
        res: dict[str,int] = {'Merlo': 2}
        self.assertEqual(mantuvieron_residencia(censo1,censo2), res)

    def test_nadie_mantuvo_residencia(self):
        censo1: dict[str,str] ={'Juan': 'Merlo', 'Ana': 'Merlo'}
        censo2: dict[str,str] = {'Juan': 'Castelar', 'Ana': 'Castelar'}
        res: dict[str,int] = {}
        self.assertEqual(mantuvieron_residencia(censo1,censo2), res)
        
    def test_tres_mantuvieron_residencia_distinta(self):
        censo1: dict[str,str] ={'Juan': 'Castelar', 'Ana': 'Merlo', 'Julia': 'Palermo'}
        censo2: dict[str,str] = {'Juan': 'Castelar', 'Ana': 'Merlo', 'Julia': 'Palermo'}
        res: dict[str,int] = { 'Castelar': 1,'Merlo': 1, 'Palermo': 1}
        self.assertEqual(mantuvieron_residencia(censo1,censo2), res)

    def test_dos_mantuvieron_residencia_distinta_dos_igual(self):
        censo1: dict[str,str] ={'Juan': 'Castelar','Marina': 'Castelar', 'Ana': 'Merlo', 'Julia': 'Palermo'}
        censo2: dict[str,str] = {'Juan': 'Castelar','Marina': 'Castelar', 'Ana': 'Merlo', 'Julia': 'Palermo'}
        res: dict[str,int] = { 'Castelar': 2,'Merlo': 1, 'Palermo': 1}
        self.assertEqual(mantuvieron_residencia(censo1,censo2), res)

if __name__ == '__main__':
    unittest.main(verbosity=2)