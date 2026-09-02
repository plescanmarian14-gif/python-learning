class Dreptunghi:
    def __init__(self,lungime,latime):
        self.lungime=lungime
        self.latime=latime
    def Aria(self):
        return self.lungime*self.latime
    def Perimetru(self):
        return 2*(self.lungime+self.latime)
    def __str__(self):
        if self.Aria()>0 and self.Perimetru()>0:
            return f"Aria este {self.Aria()}, iar perimetru {self.Perimetru()}"
        else:
            return f"valori mai mari decat 0"

drept=Dreptunghi(0,0)
print(drept)