class Masina:
    def __init__(self, marca, model, an):
        self.marca=marca
        self.model=model
        self.an=an
    def Descriere(self):
        print("Automobilul este unul foarte bun , il gasiti in garajul nostru!")
    def __str__(self):
        return f"Automobil {self.marca}, model {self.model}, din anul {self.an}"

auto1=Masina("Mercedes","AMG GT 4 doors",2026)
auto1.Descriere()
print(auto1)



