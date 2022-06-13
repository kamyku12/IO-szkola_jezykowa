from models.pracownik import pracownik


class ksiegowy(pracownik):
    def __init__(self, id, imie, nazwisko, pesel, telefon):
        super().__init__(id, imie, nazwisko, pesel, telefon)

    def edytujRachunek(self, Rachunek):
        pass
        #To Do

    def stworzRachunek(self, naleznosc, osoba, comment):
        osoba.dodajRachunek(naleznosc, comment)