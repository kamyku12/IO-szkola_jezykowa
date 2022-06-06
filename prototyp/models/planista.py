from pracownik import pracownik


class planista(pracownik):
    def __init__(self, id, imie, nazwisko, pesel, telefon):
        super().__init__(id, imie, nazwisko, pesel, telefon)

    def edytujPlanLekcji(self, plan):
        pass
        #To Do
