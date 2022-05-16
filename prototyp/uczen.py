from osoba import osoba


class uczen(osoba):
    def __init__(self, id, imie, nazwisko, pesel, telefon, grupa):
        self.id = id
        self.oceny = []
        self.grupa = grupa
        super().__init__(imie, nazwisko, pesel, telefon)

    def sprawdzOceny(self):
        pass
        # To Do
