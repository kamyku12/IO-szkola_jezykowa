import numpy as np

import ksiegowy
import nauczyciel
import planista
import uczen


def stworzUczniow():
    u = []
    for i in range(10):
        u.append(uczen.uczen(i+1, "UczenImie" + str(i+1), "UczenNazwisko" + str(i+1), "12345678901", "123456789", str(i % 3 + 1)))

    return u

def stworzNauczycieli():
    n = []
    for i in range(3):
        n.append(nauczyciel.nauczyciel(i+1, "NauczycielImie" + str(i+1), "NauczycielNazwisko" + str(i+1), "12345678901", "123456789", str(i % 3 + 1)))

    return n

def dodajOceny(nauczyciele, uczniowie):
    print("Dodawanie ocen...")
    for i in range(np.random.randint(1, 30)):
        nauczyciele[np.random.randint(0, 3)].dodajOcene(np.random.randint(1, 7), np.random.randint(1, 11), uczniowie[np.random.randint(0, 10)])


def sprawdzOceny(uczniowie):
    print("Oceny wszystkich uczniów:")
    for u in uczniowie:
        u.sprawdzOceny()


def dodajRachunki(nauczyciele, uczniowie, planista, ksiegowy):
    for n in nauczyciele:
        naleznosc = (1000.00 - 20.00) * np.random.random_sample() + 20.00
        ksiegowy.stworzRachunek(naleznosc, n)

    for u in uczniowie:
        naleznosc = (1000.00 - 20.00) * np.random.random_sample() + 20.00
        ksiegowy.stworzRachunek(naleznosc, u)

    ksiegowy.stworzRachunek((1000.00 - 20.00) * np.random.random_sample() + 20.00, planista)
    ksiegowy.stworzRachunek((1000.00 - 20.00) * np.random.random_sample() + 20.00, ksiegowy)


def pokazRachunki(nauczyciele, uczniowie, planista, ksiegowy):
    print("\nRachunki osób:")
    nauczyciele[np.random.randint(0, len(nauczyciele))].sprawdzRachunki()
    uczniowie[np.random.randint(0, len(uczniowie))].sprawdzRachunki()
    planista.sprawdzRachunki()
    ksiegowy.sprawdzRachunki()


def main():
    u = stworzUczniow()
    n = stworzNauczycieli()
    k = ksiegowy.ksiegowy("421", "Andrzej", "Ackiewicz", "82539012378", "521879023")
    p = planista.planista("901", "Barbara", "Bckiewicz", "72639012789", "523817950")
    dodajOceny(n, u)
    sprawdzOceny(u)
    dodajRachunki(n, u, p, k)
    pokazRachunki(n, u, p, k)
    # siema



if __name__ == '__main__':
    main()
