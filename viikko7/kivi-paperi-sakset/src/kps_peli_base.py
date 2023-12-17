from tuomari import Tuomari

class KpsPeli:
    def __init__ (self):
        self.tuomari = Tuomari()
        self._eka_siirto = self._read_eka_siirto()
        self._toka_siirto = self._read_toka_siirto()

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"

    def _read_eka_siirto(self):
        self._eka_siirto = input("Ensimmäisen pelaajan siirto: ")
        return self._eka_siirto

    def _lue_siirrot_(self):
        self._read_eka_siirto()
        self._read_toka_siirto()

    def _read_toka_siirto(self):
        self._toka_siirto = input("Toisen pelaajan siirto: ")
        return self._toka_siirto

    def pelaa(self):
        while self._onko_ok_siirto(self._eka_siirto) and self._onko_ok_siirto(self._toka_siirto):
            self.tuomari.kirjaa_siirto(self._eka_siirto, self._toka_siirto)
            print(self.tuomari)
            self._lue_siirrot_()
        print("Kiitos!")
        print(self.tuomari)
