import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)


    def test_kortin_saldo_alustuu_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_saldon_lataus_onnistuu(self):
        self.maksukortti.lataa_rahaa(10)
        self.assertEqual(str(self.maksukortti), "saldo: 0.2")

    def test_saldon_vahennys_onnistuu(self):
        self.maksukortti.ota_rahaa(10)
        self.assertEqual(str(self.maksukortti), "saldo: 0.0")

    def test_saldoa_ei_voi_vahentaa_alle_0(self):
        self.maksukortti.ota_rahaa(20)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_ota_rahaa_true_jos_saldo_riittaa(self):
        self.assertEqual(self.maksukortti.ota_rahaa(5), True)

    def test_ota_rahaa_false_jos_saldo_ei_riita(self):
        self.assertEqual(self.maksukortti.ota_rahaa(15), False)

