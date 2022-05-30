import rachunek


class osoba:
    def __init__(self, imie, nazwisko, pesel, telefon):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pesel = pesel
        self.telefon = telefon
        self.rachunki = []

    def sprawdzPlanLekcji(self):
        pass
        # To Do

    def dodajRachunek(self, naleznosc):
        self.rachunki.append(rachunek.rachunek(naleznosc))

    def sprawdzRachunki(self):
        print("\n" + self.ImieNazwisko())
        for r in self.rachunki:
            r.print()

    def sprawdzWplaty(self):
        print("\n" + self.ImieNazwisko())
        for r in self.rachunki:
            print(r.id)
            for w in r.wplaty:
                w.print()

    def oplacRachunek(self, rachunek, ile):
        for r in self.rachunki:
            if rachunek == r.id:
                r.oplac(ile)

    def ImieNazwisko(self):
        return self.imie + " " + self.nazwisko