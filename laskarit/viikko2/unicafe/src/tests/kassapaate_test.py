import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(400)

    def test_kassapaatteen_saldo_alussa(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_edulliset_alussa(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukkaat_alussa(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_edullinen_kateisosto_rahat_riittaa_kassa(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_edullinen_kateisosto_rahat_riittaa_maksu(self):
        maksu = self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(maksu, 60)

    def test_edullinen_kateisosto_rahat_riittaa_maara(self):
        maksu = self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_maukas_kateisosto_rahat_riittaa_kassa(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_maukas_kateisosto_rahat_riittaa_maksu(self):
        maksu = self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(maksu, 100)

    def test_maukas_kateisosto_rahat_riittaa_maara(self):
        maksu = self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_edullinen_kateisosto_rahat_eivat_riita_kassa(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_edullinen_kateisosto_rahat_eivat_riita_maksu(self):
        maksu = self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(maksu, 100)

    def test_edullinen_kateisosto_rahat_eivat_riita_maara(self):
        maksu = self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukas_kateisosto_rahat_eivat_riita_kassa(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_maukas_kateisosto_rahat_eivat_riita_maksu(self):
        maksu = self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(maksu, 200)

    def test_maukas_kateisosto_rahat_eivat_riita_maara(self):
        maksu = self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_edullinen_kortilla_rahat_riittaa_saldot(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_edullinen_kortilla_rahat_riittaa_saldot_maara(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_edullisesti_kortilla_rahat_eivat_riita_maara(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_edullinen_kortilla_rahat_riittaa(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)

    def test_edullinen_kortilla_rahat_eivat_riita(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), False)

    def test_maukkaasti_kortilla_rahat_riittaa_saldot(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_maukkaasti_kortilla_rahat_riittaa_saldot_maara(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_maukkaasti_kortilla_rahat_eivat_riita_maara(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_maukkaasti_kortilla_rahat_riittaa(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True)

    def test_maukkaasti_kortilla_rahat_eivat_riita(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), False)

    def test_kortin_lataus_kortille_kassa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100200)

    def test_kortin_lataus_kortille_negatiivinen(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kortin_lataus_kortille_nolla(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kortin_lataus_kortille_saldo(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 200)
        self.assertEqual(str(self.maksukortti), "saldo: 6.0")
