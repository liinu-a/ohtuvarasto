import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_virheellinen_saldo(self):
        virheellinen_varasto = Varasto(10, -10)

        self.assertAlmostEqual(virheellinen_varasto.saldo, 0)

    def test_saldo_ylittaa_varaston_tilavuuden(self):
        virheellinen_varasto = Varasto(10, 15)

        self.assertAlmostEqual(virheellinen_varasto.saldo, 10)

    def test_oikea_saldo_varaston_tilavuuteen_nahden(self):
        varasto_saldolla = Varasto(10, 8)

        self.assertAlmostEqual(varasto_saldolla.saldo, 8)

    def test_uudella_varastolla_virheellinen_tilavuus(self):
        virheellinen_varasto = Varasto(-10)

        self.assertAlmostEqual(virheellinen_varasto.tilavuus, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_liikaa_saldoa(self):
        self.varasto.lisaa_varastoon(15)

        self.assertAlmostEqual(self.varasto.saldo, 10)
    
    def test_lisaa_negatiivisesti_saldoa(self):
        self.varasto.lisaa_varastoon(-5)

        self.assertAlmostEqual(self.varasto.saldo, 0)

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

    def test_ottaminen_ottaa_liikaa(self):
        self.varasto.lisaa_varastoon(8)

        otettu = self.varasto.ota_varastosta(10)

        self.assertAlmostEqual(self.varasto.saldo, 0)
        self.assertAlmostEqual(otettu, 8)

    def test_virheellinen_ottaminen_negatiivisella_arvolla(self):
        otettu = self.varasto.ota_varastosta(-5)

        self.assertAlmostEqual(self.varasto.saldo, -5)
        self.assertAlmostEqual(otettu, 0)

    def test_str_toimii_oikein(self):
        self.assertAlmostEqual(str(self.varasto), "saldo = 0, vielä tilaa 10")
