from random import randint
from celle import Celle
import random

#Brukes for å teste om variablene funker
def assert_variabler(objekt, forventet_variabler):
    for variabel in forventet_variabler:
        assert hasattr(objekt, variabel), f"manglende variabel for {objekt.__class__.__name__}: {variabel}"

def assert_metoder(objekt, forventet_metoder):
    for metode in forventet_metoder:
        assert hasattr(objekt, metode), f"manglende metode for {objekt.__class__.__name__}: {metode}"

def assert_type(verdi, forventet_typen, navn):
    assert isinstance(verdi, forventet_typen), f"{navn} er av typen {type(verdi).__name__}, men \
                                                det burde være av typen {forventet_typen.__name__}"

def assert_verdi(verdi, forventet_verdi, navn):
    assert_type(verdi, type(forventet_verdi), navn)
    assert verdi == forventet_verdi, f"{navn} var {verdi} men det burde være {forventet_verdi}"









#Klassen Rutenett
class Rutenett:
    def __init__(self, rader, kolonner):
        self._ant_rader = rader
        self._ant_kolonner = kolonner
        self._rutenett = self._lag_tomt_rutenett()

    #Lager en liste fylt med None verdier
    def _lag_tom_rad(self):
        rad = []
        for i in range(self._ant_kolonner):
            rad.append(None)
        return rad

    #Setter listene fylt med None verdier sammen i en ytre liste
    def _lag_tomt_rutenett(self):
        rutenett = []
        for i in range(self._ant_rader):
            rad = self._lag_tom_rad()
            rutenett.append(rad)
        return rutenett

    #Erstatter alle None verdiene med celler
    def fyll_med_tilfeldige_celler(self):
        for rad in self._rutenett:
            index = 0
            for kolonne in rad:
                rad[index] = self.lag_celle()
                index += 1

    #Lager et celle objekt. Bruker randint for å gi cellen 1/3 sjanse for å være levende
    def lag_celle(self):
        celle = Celle()
        tall = randint(0, 2)
        if tall == 1:
            celle.sett_levende()
        return celle

    #Henter celle på angitt kordinat. Om rad eller kolonne er en ugyldig verdi blir None returnert
    def hent_celle(self, rad, kolonne):
        if rad < 0 or kolonne < 0:
            return None
        else:
            try:
                return self._rutenett[rad][kolonne]
            except IndexError:
                return None

    #Printer ut alle cellene i form av tegnet deres, som er enten '.' eller 'O',  inn i terminalen slik at det blir et brett
    def tegn_rutenett(self):
        for rad in self._rutenett:
            for kolonne in rad:
                print(kolonne.hent_status_tegn(), end="")

    #Tar imot en celles koordinater og legger alle nabocellene inn i _naboer lista
    def _sett_naboer(self, rad, kolonne):
        celle = self.hent_celle(rad, kolonne)
        nabo1 = self.hent_celle(rad-1, kolonne-1)
        nabo2 = self.hent_celle(rad, kolonne-1)
        nabo3 = self.hent_celle(rad+1, kolonne-1)
        nabo4 = self.hent_celle(rad-1, kolonne)
        nabo5 = self.hent_celle(rad+1, kolonne)
        nabo6 = self.hent_celle(rad-1, kolonne+1)
        nabo7 = self.hent_celle(rad, kolonne+1)
        nabo8 = self.hent_celle(rad+1, kolonne+1)
        naboer = [nabo1, nabo2, nabo3, nabo4, nabo5, nabo6, nabo7, nabo8]
        for nabo in naboer:
            if nabo is not None:
                celle._naboer.append(nabo)

    #Kaller på _sett_naboer for hver plass i rutenettet
    def koble_celler(self):
        for i in range(self._ant_rader):
        #f.eks blir i blir først 0, også 1, også 2....antall objekter ganger: [[none, none], [none, none], [none, none]]   Testet og fungert
            for j in range(self._ant_kolonner):
            #for kolonne in self._rutenett[i]:
                self._sett_naboer(i, j)

    #Returnerer en liste med alle celler i rutenettet
    def hent_alle_celler(self):
        liste = []
        for rad in self._rutenett:
            for celle in rad:
                liste.append(celle)
        return liste

    #Returnerer antall levende celler i rutenettet
    def antall_levende(self):
        teller = 0
        celler = self.hent_alle_celler()
        for celle in celler:
            if celle.er_levende() == True:
                teller += 1
        return teller
