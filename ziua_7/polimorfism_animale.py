class Animal:
    def __init__(self,nume):
        self.nume=nume
    def Suna(self):
        return f"Buna, sunt animal generic"
class Caine(Animal):
    def __init__(self,nume):
        super().__init__(nume)
    def Suna(self):
        return f"Buna, sunt cainele {self.nume}"
class Pisica(Animal):
    def __init__(self,nume):
        super().__init__(nume)
    def Suna(self):
        return f"Buna, sunt pisica {self.nume}"
class Vaca(Animal):
    def __init__(self,nume):
        super().__init__(nume)
    def Suna(self):
        return f"Buna, sunt vaca {self.nume}"
animal=Animal("Bou")
caine=Caine("Caine")
pisica=Pisica("Pisica")
vaca=Vaca("Vaca")
animale=[caine,pisica,vaca]
for f in animale:
    print(f.Suna())