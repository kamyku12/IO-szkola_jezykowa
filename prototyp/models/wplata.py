import datetime


class wplata:
    def __init__(self, kwota):
        self.kwota = kwota
        self.data = datetime.date.today()

    def __str__(self):
        return "\nKwota - " + str(self.kwota) + "\nData - " + str(self.data)