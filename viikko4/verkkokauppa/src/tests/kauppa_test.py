import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()
        self.viitegeneraattori_mock.uusi.side_effect = [42, 69]
        self.varasto_mock = Mock()

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return 10
            if tuote_id == 3:
                return 0

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(1, "turbomaito", 15)
            if tuote_id == 3:
                return Tuote(1, "kaurajuoma", 10)

        # otetaan toteutukset käyttöön
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        self.kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)


    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):


        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_ostoksen_paatyttya_pankin_methodia_tilimaksu_kutsutaan_asiakkaalla_tilinrolla_ja_summalla(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu oikeilla parametreilla 
        self.pankki_mock.tilisiirto.assert_called_with('pekka', 42, '12345', '33333-44455', 5)
        # nyt välitetään kutsuun liittyvistä argumenteista :) 

    
    def test_ostoksen_paatuttua_pankin_methodia_tilimaksu_kutsutaan_asiakkaalla_tilinrolla_ja_summalla_eri_tuotteilla(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu oikeilla parametreilla 
        self.pankki_mock.tilisiirto.assert_called_with('pekka', 42, '12345', '33333-44455', 20)
        # nyt välitetään kutsuun liittyvistä argumenteista :) 

    def test_ostoksen_paatuttua_pankin_methodia_tilimaksu_kutsutaan_asiakkaalla_tilinrolla_ja_summalla_2_samaa_tuotetta(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu oikeilla parametreilla 
        self.pankki_mock.tilisiirto.assert_called_with('pekka', 42, '12345', '33333-44455', 30)
        # nyt välitetään kutsuun liittyvistä argumenteista :) 

    def test_ostoksen_paatuttua_pankin_methodia_tilimaksu_kutsutaan_asiakkaalla_tilinrolla_ja_toinen_tuote_loppu(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu oikeilla parametreilla 
        self.pankki_mock.tilisiirto.assert_called_with('pekka', 42, '12345', '33333-44455', 5)
        # nyt välitetään kutsuun liittyvistä argumenteista :) 

    def test_seuraava_ostos_nollaa_edellisen_tiedot_ja_palauttaa_uuden_tiedot(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # seuraava asiakas 

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("kalle", "67890")
        self.pankki_mock.tilisiirto.assert_called_with('kalle', 69, '67890', '33333-44455', 15)

    def test_tuotteen_poistaminen_ostoskorista_poistaa_tuotteen_yhdesti_usemapi_tuote(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.poista_korista(1)

        self.kauppa.tilimaksu("pekka", "67890")
        self.pankki_mock.tilisiirto.assert_called_with('pekka', 42, '67890', '33333-44455', 5)

    def test_tuotteen_poistaminen_ostoskorista_palauttaa_tuotteen_varastoon(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.poista_korista(1)

        self.kauppa.tilimaksu("pekka", "67890")
        self.varasto_mock.palauta_varastoon.assert_called_with(Tuote(1, "maito", 5))