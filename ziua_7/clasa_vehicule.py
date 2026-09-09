class Vehicul:
    def __init__(self,marca,viteza_maxima):
        self.marca=marca
        self.viteza_maxima=viteza_maxima
    def __str__(self):
        return f"Marca: {self.marca} si viteza: {self.viteza_maxima}"
class Motocicleta(Vehicul):
    def __init__(self,marca,viteza_maxima,motor):
        super().__init__(marca,viteza_maxima)
        self.motor=motor
    def __str__(self):
        return f" Marca este {self.marca},cu viteza maxima de {self.viteza_maxima} si cu motor de {self.motor} "


class Masina(Vehicul):
    def __init__(self, marca, viteza_maxima, numar_usi):
        super().__init__(marca, viteza_maxima)
        self.numar_usi = numar_usi

    def __str__(self):
        return f" Marca este {self.marca},cu viteza maxima de {self.viteza_maxima} si cu {self.numar_usi} usi"

vehicul=Vehicul("Bmw",180)
motocicleta=Motocicleta("Bmw",180,3.0)
masina=Masina("Bmw",200,1.5)
forma=[vehicul,motocicleta,masina]
for f in forma:
    print(f"{f}")