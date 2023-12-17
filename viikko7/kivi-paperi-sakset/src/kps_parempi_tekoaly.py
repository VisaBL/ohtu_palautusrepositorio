from kps_peli_base import KpsPeli
from tekoaly_parannettu import TekoalyParannettu

class VaikeaTekoalypeli(KpsPeli):
    def __init__(self):
        self._tekoaly = TekoalyParannettu(10)
        super().__init__()
        
    def _read_toka_siirto(self):
        self._toka_siirto = self._tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {self._toka_siirto}")
        self._tekoaly.aseta_siirto(self._eka_siirto)
        return self._toka_siirto