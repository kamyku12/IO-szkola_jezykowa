class zajecie:
    def __init__(self, data, od, do, grupa, nazwa, nauczyciel):
        self.data = data
        self.od = od
        self.do = do
        self.grupa = grupa
        self.nazwa = nazwa
        self.nauczyciel = nauczyciel

    def __str__(self):
        return "\nData - " + str(self.data) + "\nOd - " + str(self.od) + "\nDo - " + "\nNazwa zajęć - " + str(
            self.nazwa) + "\nNauczyciel - " + str(self.nauczyciel) + "\nGrupa - " + str(self.grupa)
