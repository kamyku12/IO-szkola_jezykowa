import numpy as np


from models.ksiegowy import ksiegowy
from models.nauczyciel import nauczyciel
from models.planista import planista
from models.uczen import uczen


def stworzUczniow():
    u = []
    for i in range(10):
        u.append(uczen(i+1, "UczenImie" + str(i+1), "UczenNazwisko" + str(i+1), "12345678901", "123456789", str(i % 3 + 1)))

    return u

def stworzNauczycieli():
    n = []
    for i in range(3):
        n.append(nauczyciel(i+1, "NauczycielImie" + str(i+1), "NauczycielNazwisko" + str(i+1), "12345678901", "123456789", str(i % 3 + 1)))

    return n

def dodajOceny(nauczyciele, uczniowie):
    print("\nDodawanie ocen...")
    for i in range(np.random.randint(1, 30)):
        nauczyciele[np.random.randint(0, 3)].dodajOcene(np.random.randint(0, 8), np.random.randint(0, 12), uczniowie[np.random.randint(0, 10)])
    print("------------------")

def sprawdzOceny(uczniowie):
    print("\nOceny wszystkich uczniów:")
    for u in uczniowie:
        u.sprawdzOceny()

    print("-------------------------")


def dodajRachunki(nauczyciele, uczniowie, planista, ksiegowy):
    print("\nDodawanie rachunków...")
    for n in nauczyciele:
        naleznosc = (1000.00 + 1000.00) * np.random.random_sample() - 100.00
        ksiegowy.stworzRachunek(naleznosc, n, "Rachunek nauczyciela")

    for u in uczniowie:
        naleznosc = (1000.00 + 100.00) * np.random.random_sample() - 100.00
        ksiegowy.stworzRachunek(naleznosc, u, "Rachunek ucznia")

    ksiegowy.stworzRachunek((1000.00 + 1000.00) * np.random.random_sample() - 1000.00, planista, "Rachunek planisty")
    ksiegowy.stworzRachunek((1000.00 + 1000.00) * np.random.random_sample() - 1000.00, ksiegowy, "Rachunek ksiegowego")
    print("-------------------------")

def pokazRachunki(nauczyciele, uczniowie, planista, ksiegowy):
    print("\nRachunki osób:")
    nauczyciele[np.random.randint(0, len(nauczyciele))].sprawdzRachunki()
    uczniowie[np.random.randint(0, len(uczniowie))].sprawdzRachunki()
    planista.sprawdzRachunki()
    ksiegowy.sprawdzRachunki()
    print("-----------------")


def main():
    u = stworzUczniow()
    n = stworzNauczycieli()
    k = ksiegowy("421", "Andrzej", "Ackiewicz", "82539012378", "521879023")
    p = planista("901", "Barbara", "Bckiewicz", "72639012789", "523817950")
    dodajOceny(n, u)
    sprawdzOceny(u)
    dodajRachunki(n, u, p, k)
    pokazRachunki(n, u, p, k)


if __name__ == '__main__':
    main()
