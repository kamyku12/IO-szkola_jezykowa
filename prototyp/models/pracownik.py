from models.osoba import osoba


class pracownik(osoba):
    def __init__(self, id, imie, nazwisko, pesel, telefon):
        self.id = id
        super().__init__(imie, nazwisko, pesel, telefon)

