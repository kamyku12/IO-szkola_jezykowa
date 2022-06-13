class ocena:
    def __init__(self, stopien, waga, nauczyciel):
        self.stopien = stopien
        self.waga = waga
        self.nauczyciel = nauczyciel

    def __str__(self):
        return "Stopień - " + str(self.stopien) + "\nWaga - " + str(self.waga) + "\nNauczyciel - " + str(self.nauczyciel)