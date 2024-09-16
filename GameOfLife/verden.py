from rutenett import Rutenett


def assert_variabler(objekt, forventet_variabler):
    for variabel in forventet_variabler:
        assert hasattr(objekt, variabel), f"manglende variabel for {objekt.__class__.__name__}: {variabel}"

def assert_metoder(objekt, forventet_metoder):
    for metode in forventet_metoder:
        assert hasattr(objekt, metode), f"manglende metode for {objekt.__class__.__name__}: {metode}"

# ----- Metodene over er kun hjelpemetoder som bruker inne i testene


class Verden:
    def __init__(self, rader, kolonner):
        self._rutenett = Rutenett(rader, kolonner)
        self._rutenett.fyll_med_tilfeldige_celler()
        self._rutenett.koble_celler()
        self._generasjonsnummer = 0


    def tegn(self):
        print(self._rutenett.tegn_rutenett())
        print("Generasjonsnummeret:", self._generasjonsnummer, " - Antall levende celler:", self._rutenett.antall_levende())

    def oppdatering(self):
        self._generasjonsnummer += 1
        for rad in self._rutenett._rutenett:
            for kolonne in rad:
                kolonne.tell_levende_naboer()
                kolonne.oppdater_status()
