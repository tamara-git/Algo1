import unittest

from torneo_de_gallinas import torneo_de_gallinas

class Test_torneo_de_gallinas(unittest.TestCase):
    def test_una_desvia_la_otra_no(self):
        estrategias: dict[str,str] = {
            "Bruny": "me la banco y no me desvío",
            "Kiara": "me desvío siempre"
        }

        res: dict[str,int] = {
            "Bruny": 10,
            "Kiara": -15
        }
        
        self.assertEqual(torneo_de_gallinas(estrategias), res)

    def test_las_dos_se_desvian(self):
        estrategias: dict[str,str] = {
            "Bruny": "me desvío siempre",
            "Kiara": "me desvío siempre"
        }

        res: dict[str,int] = {
            "Bruny": -10,
            "Kiara": -10

        }

        self.assertEqual(torneo_de_gallinas(estrategias), res)

    def test_ninguna_se_desvia(self):
        estrategias: dict[str,str] = {
            "Bruny": "me la banco y no me desvío",
            "Kiara": "me la banco y no me desvío"
        }

        res: dict[str,int] = {
            "Bruny": -5,
            "Kiara": -5

        }

        self.assertEqual(torneo_de_gallinas(estrategias), res)

    def test_dos_desvios_y_uno_no(self):
        estrategias: dict[str,str] = {
            "Bruny": "me desvío siempre", 
            "Kiara": "me desvío siempre",
            "Pablo": "me la banco y no me desvío"
        }

        res: dict[str,int] = {
            "Bruny": -25,
            "Kiara": -25,
            "Pablo": 20

        }

        self.assertEqual(torneo_de_gallinas(estrategias), res)
