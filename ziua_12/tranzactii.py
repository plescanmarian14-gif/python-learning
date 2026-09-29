from datetime import datetime


class Tranzactie:
    def __init__(self, suma, descriere, data=None):
        self.suma = suma
        self.descriere = descriere
        self.data = data if data else datetime.now()

    def __str__(self):
        return f"{self.data.strftime('%Y-%m-%d %H:%M:%S')} | {self.descriere} | {self.suma} RON"

    def to_dict(self):
        return {
            "suma": self.suma,
            "descriere": self.descriere,
            "data": self.data.strftime("%Y-%m-%d %H:%M:%S"),
            "tip": "tranzactie"
        }


class Venit(Tranzactie):
    def __init__(self, suma, descriere, sursa, data=None):
        super().__init__(suma, descriere, data)
        self.sursa = sursa

    def __str__(self):
        return f"[VENIT] {self.descriere} ({self.sursa}): +{self.suma} RON"

    def to_dict(self):
        d = super().to_dict()
        d["sursa"] = self.sursa
        d["tip"] = "venit"
        return d


class Cheltuiala(Tranzactie):
    def __init__(self, suma, descriere, categorie, data=None):
        super().__init__(suma, descriere, data)
        self.categorie = categorie

    def __str__(self):
        return f"[CHELTUIALĂ] {self.descriere} [{self.categorie}]: -{self.suma} RON"

    def to_dict(self):
        d = super().to_dict()
        d["categorie"] = self.categorie
        d["tip"] = "cheltuiala"
        return d