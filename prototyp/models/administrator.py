from pracownik import pracownik


class administrator(pracownik):
    def __init__(self, id, imie, nazwisko, pesel, telefon):
        super().__init__(id, imie, nazwisko, pesel, telefon)

    def dodajUcznia(self, id, imie, nazwisko, pesel, telefon, grupa):
        pass
        # To Do

    def dodajNauczyciela(self, id, imie, nazwisko, pesel, telefon, wychowawca):
        pass
        # To Do

    def dodajKsiegowego(self, id, imie, nazwisko, pesel, telefon):
        pass
        # To Do

    def dodajPlaniste(self, id, imie, nazwisko, pesel, telefon):
        pass
        # To Do