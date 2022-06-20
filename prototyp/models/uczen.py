from models.ocena import ocena
from models.osoba import osoba


class uczen(osoba):
    def __init__(self, id, imie, nazwisko, pesel, telefon, grupa):
        self.id = id
        self.oceny = []
        self.grupa = grupa
        super().__init__(imie, nazwisko, pesel, telefon)

    def sprawdzOceny(self):
        print(self)
        if self.oceny:
            for o in self.oceny:
                print(o)
            return
        else:
            print("Brak ocen")
            return

    def dodajOcene(self, stopien, waga, nauczyciel, komentarz):
        if stopien < 1 or stopien > 6:
            raise ValueError("Nieprawidlowy stopien")

        if waga < 1 or waga > 10:
            raise ValueError("Nieprawidlowa waga oceny")

        self.oceny.append(ocena(stopien, waga, nauczyciel, komentarz))
        print("Dodano ocenę")
        return

    def __str__(self):
        return "\n" + self.imie + " " + self.nazwisko