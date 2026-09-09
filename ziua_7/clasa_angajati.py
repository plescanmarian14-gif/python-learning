class Angajat:
    def __init__(self,nume,salariu):
        self.nume=nume
        self.salariu=salariu
    def descriere(self):
        return f"{self.nume}, salariu {self.salariu}"
class Manager(Angajat):
    def __init__(self,nume,salariu,echipa_marime):
        super().__init__(nume,salariu)
        self.echipa_marime=echipa_marime
    def descriere(self):
        return f"{super().descriere()},coordoneaza {self.echipa_marime} oameni"
class Dezvoltator(Manager):
    def __init__(self,nume,salariu,echipa_marime,limbaj_principal):
        super().__init__(nume,salariu,echipa_marime)
        self.limbaj_principal=limbaj_principal
    def descriere(self):
        return f"{super().descriere()}, vorbeste in limba {self.limbaj_principal}"


m=Dezvoltator("Ana",8000,5,"Romana")
print(m.descriere())