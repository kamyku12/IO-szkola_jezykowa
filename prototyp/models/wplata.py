import datetime


class wplata:
    def __init__(self, kwota):
        self.kwota = kwota
        self.data = datetime.date.today()

    def print(self):
        print("Kwota - " + self.kwota)
        print("Data - " + str(self.data))

    def __str__(self):
        return "Kwota - " + str(self.kwota) + "\nData - " + str(self.data)