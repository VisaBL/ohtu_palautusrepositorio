from kps_peli_base import KpsPeli
from kps_parempi_tekoaly import VaikeaTekoalypeli
from kps_tekoaly import Tekoalypeli

class KpsPelinRakentaja:
    def __init__(self):
        self._game = None

    def luo_peli(self, vastaus):
        if vastaus.endswith("a"):
            return KpsPeli()
        elif vastaus.endswith("b"):
            return Tekoalypeli()
        elif vastaus.endswith("c"):
            return VaikeaTekoalypeli()
        
        return False
        
    def tulosta_ohjeet(self):
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
               )

    def alusta_peli(self):
        while True:
            self.tulosta_ohjeet()
            vastaus = input()
            self._game = self.luo_peli(vastaus)
            if not self._game:
                break
            self._game.pelaa()
        
