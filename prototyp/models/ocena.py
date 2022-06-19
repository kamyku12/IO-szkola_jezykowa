import datetime as dt

class ocena:
    def __init__(self, stopien, waga, nauczyciel, komentarz):
        self.stopien = stopien
        self.waga = waga
        self.nauczyciel = nauczyciel
        self.komentarz = komentarz
        self.data = dt.date.today()

    def __str__(self):
        return ("Stopień - " + str(self.stopien) +
                "\nWaga - " + str(self.waga) +
                "\nWystawiający - " + str(self.nauczyciel) +
                "\nKomentarz - " + self.komentarz +
                "\nData - " + str(self.data) + "\n")