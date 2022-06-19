import numpy as np
from models.administrator import administrator


def stworzGrupy(admin, nauczyciele):
    print("\nTworzenie grup")
    g = []
    for i in range(3):
        g.append(admin.dodajGrupe("Grupa" + str(i),
                                  nauczyciele[np.random.randint(0, len(nauczyciele))]))
    print("------------------")
    return g


def stworzUczniow(admin, grupy):
    print("\nTworzenie uczniow")
    for i in range(40):
        admin.dodajUcznia(i + 1, "UczenImie" + str(i + 1),
                          "UczenNazwisko" + str(i + 1),
                          "12345678901",
                          "123456789",
                          grupy[np.random.randint(0, len(grupy))])
    print("--------------------")


def stworzNauczycieli(admin):
    print("\nTworzenie nauczycieli...")
    n = []
    for i in range(3):
        n.append(admin.dodajNauczyciela(i + 1,
                                        "NauczycielImie" + str(i + 1),
                                        "NauczycielNazwisko" + str(i + 1),
                                        "12345678901",
                                        "123456789"))
    print("-----------------------")
    return n


def pokazGrupy(grupy):
    print("\nWykaz Grup...")
    for g in grupy:
        g.pokaz()
    print("----------------")


def dodajOceny(nauczyciele, grupy):
    print("\nDodawanie ocen...")
    for i in range(np.random.randint(1, 30)):
        for g in grupy:
            if(g.uczniowie):
                nauczyciele[np.random.randint(0, 3)].dodajOcene(np.random.randint(0, 8),
                                                                np.random.randint(0, 12),
                                                                g.uczniowie[np.random.randint(0, len(g.uczniowie))],
                                                                "Komentarz " + str(i))
    print("------------------")


def sprawdzOceny(grupy):
    print("\nOceny wszystkich uczniów:")
    for g in grupy:
        for u in g.uczniowie:
            u.sprawdzOceny()
    print("-------------------------")


def dodajRachunki(nauczyciele, grupy, planista, ksiegowy, admin):
    print("\nDodawanie rachunków...")
    for n in nauczyciele:
        naleznosc = (1000.00 + 100.00) * np.random.random_sample() - 100.00
        ksiegowy.stworzRachunek(naleznosc,
                                n,
                                "Rachunek nauczyciela")

    for g in grupy:
        for u in g.uczniowie:
            naleznosc = (1000.00 + 100.00) * np.random.random_sample() - 100.00
            ksiegowy.stworzRachunek(naleznosc,
                                    u,
                                    "Rachunek ucznia")

    ksiegowy.stworzRachunek((1000.00 + 100.00) * np.random.random_sample() - 100.00,
                            planista,
                            "Rachunek planisty")
    ksiegowy.stworzRachunek((1000.00 + 100.00) * np.random.random_sample() - 100.00,
                            ksiegowy,
                            "Rachunek ksiegowego")
    ksiegowy.stworzRachunek((1000.00 + 100.00) * np.random.random_sample() - 100.00,
                            admin,
                            "Rachunek administratora")
    print("-------------------------")


def pokazRachunki(nauczyciele, grupy, planista, ksiegowy, admin):
    print("\nRachunki osób:")
    nauczyciele[np.random.randint(0, len(nauczyciele))].sprawdzRachunki()
    for g in grupy:
        g.uczniowie[np.random.randint(0, len(g.uczniowie))].sprawdzRachunki()
    planista.sprawdzRachunki()
    ksiegowy.sprawdzRachunki()
    admin.sprawdzRachunki()
    print("-----------------")


def main():
    admin = administrator(1,
                          "Admin",
                          "Adminowicz",
                          "82749301231",
                          "123456789")
    n = stworzNauczycieli(admin)
    g = stworzGrupy(admin, n)
    stworzUczniow(admin, g)
    pokazGrupy(g)
    k = admin.dodajKsiegowego("421",
                              "Andrzej",
                              "Ackiewicz",
                              "82539012378",
                              "521879023")
    p = admin.dodajPlaniste("901",
                            "Barbara",
                            "Bckiewicz",
                            "72639012789",
                            "523817950")
    dodajOceny(n, g)
    sprawdzOceny(g)
    dodajRachunki(n, g, p, k, admin)
    pokazRachunki(n, g, p, k, admin)


if __name__ == '__main__':
    main()
