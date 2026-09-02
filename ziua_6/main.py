# class Persoana:
#     def __init__(self,nume,varsta):
#         self.nume=nume
#         self.varsta=varsta
#     def afisare(self):
#         print(f"Numele meu este {self.nume} si am {self.varsta} de ani")
#
# persoana1=Persoana("Marian",25)
# persoana2=Persoana("Paul",12)
# print(persoana1.afisare())
# print(persoana2.afisare())

class Cont:
    def __init__(self,titular,sold=0):
        self.titular=titular
        self.sold=sold
    def adauga(self,suma):
        self.sold+=suma
    def __str__(self):
        return f"Soldul titularului {self.titular} este in valoare de {self.sold}"

persoana=Cont("Marian",100)
persoana.adauga(120)
print(persoana)

