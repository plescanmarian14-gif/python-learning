import math
class Forma:
    def __init__(self,lungime):
        self.lungime=lungime
    def Arie(self):
        return 0

class Dreptunghi(Forma):
    def __init__(self,lungime,latime):
        super().__init__(lungime)
        self.latime=latime
    def Arie(self):
        return self.lungime*self.latime
class Cerc(Forma):
    def __init__(self,lungime):
        super().__init__(lungime)
    def Arie(self):
        return 3.14*(self.lungime/2**2)

forma=Forma(30)
drept=Dreptunghi(20,10)
cerc=Cerc(10)
form=[forma,drept,cerc]
for f in form:
    print(f"Ariile sunt:{f.Arie()}")