import ocena
from osoba import osoba


class uczen(osoba):
    def __init__(self, id, imie, nazwisko, pesel, telefon, grupa):
        self.id = id
        self.oceny = []
        self.grupa = grupa
        super().__init__(imie, nazwisko, pesel, telefon)

    def sprawdzOceny(self):
        print("\n" + self.imie + " " + self.nazwisko)
        if self.oceny:
            for o in self.oceny:
                o.print()
            return
        else:
            print("Brak ocen")
            return



    def dodajOcene(self, stopien, waga, nauczyciel):
        self.oceny.append(ocena.ocena(stopien, waga, nauczyciel))