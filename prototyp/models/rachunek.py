import datetime as dt
import numpy as np

from models.wplata import wplata


class rachunek():
    def __init__(self, naleznosc, comment):
        self.id = np.random.randint(100, 2000)
        self.naleznosc = round(naleznosc, 2)
        self.saldo = -round(naleznosc, 2)
        self.oplacone = False
        self.termin = dt.date.today() + dt.timedelta(days=90)
        self.wplaty = []
        self.comment = comment


    def oplac(self, ile):
        if ile <= 0.00:
            print("Nie można utworzyć wpłaty dla wartości mniejszych lub równych 0.00zł")
            return

        self.wplaty.append(wplata(ile))
        self.saldo = self.saldo + ile
        if self.saldo > 0:
            print("Przelano za dużo, zwracamy " + self.saldo + " nadplaty")
            self.oplacone = True
            self.saldo = 0
        elif self.saldo == 0:
            self.oplacone = True
        return

    def __str__(self):
        return "Id - " + str(self.id) + "\nNależność - " + str(self.naleznosc) + \
               "\nSaldo - " + str(self.saldo) + "\nKomentarz - " + str(self.comment)
