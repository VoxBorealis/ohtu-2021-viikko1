import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_alku_tilavuus_oikein(self):
        self.varasto = Varasto(-1)
        self.assertAlmostEqual(self.varasto.tilavuus, 0.0)

    def test_alku_saldo_virheellinen(self):
        self.varasto = Varasto(10, alku_saldo = -1)
        self.assertAlmostEqual(self.varasto.saldo, 0.0)

    def test_lisaa_varastoon_negatiivinen(self):
        sld = self.varasto.saldo
        self.varasto.lisaa_varastoon(-5)
        self.assertAlmostEqual(sld, self.varasto.saldo)
    
    def test_lisaa_varastoon_liikaa(self):
        self.varasto.lisaa_varastoon(100)
        self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_ota_varastosta_negatiivinen(self):
        self.assertAlmostEqual(self.varasto.ota_varastosta(-10), 0.0)

    def test_ota_varastosta_liikaa(self):
        self.varasto.lisaa_varastoon(5)
        sld = self.varasto.saldo
        self.assertAlmostEqual(self.varasto.ota_varastosta(20), sld)
    
    def test_string_palautus(self):
        self.varasto.lisaa_varastoon(5)
        
        self.assertAlmostEqual(self.varasto.__str__(), "saldo = 5, vielä tilaa 5")
