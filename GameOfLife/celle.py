class Celle:
    def __init__(self):
        self._status = "doed"
        self._naboer = []
        self._ant_levende_naboer = 0

    def sett_doed(self):
        self._status = "doed"

    def sett_levende(self):
        self._status = "levende"

    def er_levende(self):
        if self._status == "levende":
            return True
        else:
            return False

    def hent_status_tegn(self):
        if self._status == "levende":
            return "O"
        if self._status == "doed":
            return "."

    def legg_til_nabo(self, nabo):
        self._naboer.append(nabo)

    def tell_levende_naboer(self):
        self._ant_levende_naboer = 0
        for nabo in self._naboer:
            if nabo.er_levende() == True:
                self._ant_levende_naboer += 1

    def oppdater_status(self):
        self.tell_levende_naboer()
        if self._status == "levende":
            if self._ant_levende_naboer < 2:
                self.sett_doed()
            if self._ant_levende_naboer > 3:
                self.sett_doed()
        if self._status == "doed":
            if self._ant_levende_naboer == 3:
                self.sett_levende()
