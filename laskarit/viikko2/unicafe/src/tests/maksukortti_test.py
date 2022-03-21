import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_on_oikein_alussa(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_rahan_lataaminen_kasvattaa_saldoa(self):
        self.maksukortti.lataa_rahaa(40)
        self.assertEqual(str(self.maksukortti), "saldo: 0.5")

    def test_saldo_vahenee_oikein(self):
        self.maksukortti.lataa_rahaa(40)
        self.maksukortti.ota_rahaa(30)
        self.assertEqual(str(self.maksukortti), "saldo: 0.2")

    def test_saldo_ei_vahene_jos_ei_saldoa(self):
        self.maksukortti.ota_rahaa(20)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")
    
    def test_palautus_jos_saldo_riittaa(self):
        self.assertEqual(self.maksukortti.ota_rahaa(10), True)
    
    def test_palautus_jos_saldo_ei_riita(self):
        self.assertEqual(self.maksukortti.ota_rahaa(20), False)