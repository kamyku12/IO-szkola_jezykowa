from models.pracownik import pracownik


class nauczyciel(pracownik):
    def __init__(self, id, imie, nazwisko, pesel, telefon, wychowawca):
        self.wychowawca = wychowawca
        super().__init__(id, imie, nazwisko, pesel, telefon)

    def dodajOcene(self, stopien, waga, uczen):
        uczen.dodajOcene(stopien, waga, self)

    def edytujOcene(self, ocena):
        pass
        #To Do

    def sprawdzOceny(self, uczen):
        uczen.sprawdzOceny()

    def sprawdzObecnosc(self, grupa):
        pass
        #To Do

    def edytujObecnosc(self, obecnosc):
        pass
        #To Do

    def __str__(self):
        return self.imie + " " + self.nazwisko