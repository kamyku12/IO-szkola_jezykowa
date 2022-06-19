from models.ksiegowy import ksiegowy
from models.nauczyciel import nauczyciel
from models.planista import planista
from models.pracownik import pracownik
from models.grupa import grupa
from models.uczen import uczen


class administrator(pracownik):
    def __init__(self, id, imie, nazwisko, pesel, telefon):
        super().__init__(id, imie, nazwisko, pesel, telefon)

    def dodajUcznia(self, id, imie, nazwisko, pesel, telefon, grupa):
        u = uczen(id, imie, nazwisko, pesel, telefon, grupa)
        grupa.dodajUcznia(u)
        return u

    def dodajGrupe(self, nazwa, nauczyciel):
        g = grupa(nazwa, nauczyciel)
        nauczyciel.wychowawca = g
        return g

    def dodajUczniaDoGrupy(self, uczen, grupa):
        grupa.uczniowie.append(uczen)
        uczen.grupa = grupa
        return

    def usunUczniaZGrupy(self, uczen, grupa):
        grupa.uczniowie.remove(uczen)
        uczen.grupa = None
        return

    def przypiszWychowawceGrupy(self, nauczyciel, grupa):
        grupa.wychowawca = nauczyciel
        return

    def dodajNauczyciela(self, id, imie, nazwisko, pesel, telefon):
        return nauczyciel(id, imie, nazwisko, pesel, telefon)

    def dodajKsiegowego(self, id, imie, nazwisko, pesel, telefon):
        return ksiegowy(id, imie, nazwisko, pesel, telefon)

    def dodajPlaniste(self, id, imie, nazwisko, pesel, telefon):
        return planista(id, imie, nazwisko, pesel, telefon)


