class Ostoskori:
    def __init__(self):
        self._tuotteet = []
    
    def lisaa(self, tuote):
        self._tuotteet.append(tuote)
    
    def poista(self, tuote):
        #funktio poistaa vain yhden tuotteen vaikka tuotetta olisi useampi sama tuote ostoskorissa
        tuotteet = []
        removed = False
        for item in self._tuotteet:
            if item.id == tuote.id and removed is False:
                removed = True
                continue
            tuotteet.append(tuote)
        self._tuotteet = tuotteet


    def hinta(self):
        hinnat = map(lambda t: t.hinta, self._tuotteet)

        return sum(hinnat)
