import datetime as dt
import numpy as np

import wplata


class rachunek():
    def __init__(self, naleznosc):
        self.id = np.random.randint(100, 2000)
        self.naleznosc = round(naleznosc, 2)
        self.saldo = -round(naleznosc, 2)
        self.oplacone = False
        self.termin = dt.date.today() + dt.timedelta(days=90)
        self.wplaty = []


    def oplac(self, ile):
        if ile <= 0.00:
            print("Nie można utworzyć wpłaty dla wartości mniejszych lub równych 0.00zł")
            return

        self.wplaty.append(wplata.wplata(ile))
        self.saldo = self.saldo + ile
        if self.saldo > 0:
            print("Przelano za dużo, zwracamy " + self.saldo + " nadplaty")
            self.oplacone = True
            self.saldo = 0
        elif self.saldo == 0:
            self.oplacone = True
        return

    def __str__(self):
        return "Id - " + self.id + "\nNależność - " + self.naleznosc + "\nSaldo - " + self.saldo

    def print(self):
        print("Id - " + self.id)
        print("Należnosc - " + self.naleznosc)
        print("Saldo - " + self.saldo)
        if self.oplacone:
            print("Oplacone - tak")
        else:
            print("Oplacone - nie")
        print("Termin - " + str(self.termin)