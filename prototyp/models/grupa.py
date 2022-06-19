class grupa:
    def __init__(self, nazwa, wychowawca):
        self.uczniowie = []
        self.nazwa = nazwa
        self.wychowawca = wychowawca

    def dodajUcznia(self, uczen):
        self.uczniowie.append(uczen)

    def zmienWychowawce(self, nauczyciel):
        self.wychowawca = nauczyciel

    def __str__(self):
        return "\nNazwa grupy: " + str(self.nazwa)

    def pokaz(self):
        print(self)
        print("Nauczyciel: " + str(self.wychowawca))
        print("Uczniowie:")
        for u in self.uczniowie:
            print(u)
