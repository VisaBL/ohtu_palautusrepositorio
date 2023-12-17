from tekoaly import Tekoaly
from kps_peli_base import KpsPeli

class Tekoalypeli(KpsPeli):
    def __init__(self):
        self._tekoaly = Tekoaly()
        super().__init__()
        
    def _read_toka_siirto(self):
        self._toka_siirto = self._tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {self._toka_siirto}")
        return self._toka_siirto
    