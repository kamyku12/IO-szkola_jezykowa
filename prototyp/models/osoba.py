from models.rachunek import rachunek


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

    def dodajRachunek(self, naleznosc, comment):
        if naleznosc <= 0.00:
            raise ValueError("Należność nie może być wartością mniejszą lub równą zero")

        self.rachunki.append(rachunek(naleznosc, comment))

    def sprawdzRachunki(self):
        print(self)
        if self.rachunki:
            for r in self.rachunki:
                print(r)
            return
        else:
            print("Brak rachunków")
            return



    def sprawdzWplaty(self):
        print(self)
        for r in self.rachunki:
            print(r.id)
            for w in r.wplaty:
                print(w)

    def oplacRachunek(self, rachunek, ile):
        for r in self.rachunki:
            if rachunek == r.id:
                r.oplac(ile)

    def __str__(self):
        return "\n" + self.imie + " " + self.nazwisko