from verden import Verden


rader = int(input("Oppgi antall rader i spillebrettet"))
kolonner = int(input("Oppgi antall kolonner i spillebrettet"))

min_verden = Verden(rader, kolonner)
min_verden.tegn()

svar = input("Trykk enter for aa fortsette. Oppgi q og trykk enter for å avslutte programmet")
while svar != "q":
    min_verden.oppdatering()
    min_verden.tegn()
    svar = input("Trykk enter for aa fortsette. Oppgi q og trykk enter for å avslutte programmet")
