from models.ocena import ocena
from models.osoba import osoba


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
                print(o)
            return
        else:
            print("Brak ocen")
            return




    def dodajOcene(self, stopien, waga, nauczyciel):
        if stopien < 1 or stopien > 6:
            print("Nieprawidlowy stopien")
            return

        if waga < 1 or waga > 10:
            print("Nieprawidlowa waga oceny")
            return

        self.oceny.append(ocena(stopien, waga, nauczyciel))
        print("Dodano ocenę")
        return