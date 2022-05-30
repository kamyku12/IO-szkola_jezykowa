class ocena:
    def __init__(self, stopien, waga, nauczyciel):
        self.stopien = stopien
        self.waga = waga
        self.nauczyciel = nauczyciel

    def print(self):
        print("Stopien - ", self.stopien)
        print("Waga - ", self.waga)
        print("Nauczyciel - ", self.nauczyciel.ImieNazwisko())