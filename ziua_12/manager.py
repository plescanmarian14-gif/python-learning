import json
from tranzactii import Tranzactie, Venit, Cheltuiala
from utils import logheaza_actiune


class ManagerFinanciar:
    def __init__(self):
        self.tranzactii = []

    @logheaza_actiune
    def adauga_tranzactie(self, tranzactie):
        self.tranzactii.append(tranzactie)

    @logheaza_actiune
    def sterge_tranzactie(self, index):
        if 0 <= index < len(self.tranzactii):
            self.tranzactii.pop(index)
        else:
            raise IndexError("Indexul introdus nu exista!")

    def total_venituri(self):
        return sum(t.suma for t in self.tranzactii if isinstance(t, Venit))

    def total_cheltuieli(self):
        return sum(t.suma for t in self.tranzactii if isinstance(t, Cheltuiala))

    def sold(self):
        return self.total_venituri() - self.total_cheltuieli()

    def filtreaza_dupa_categorie(self, categorie):
        return list(
            filter(
                lambda t: isinstance(t, Cheltuiala) and t.categorie.lower() == categorie.lower(),
                self.tranzactii
            )
        )

    def top_cheltuieli(self, n):
        cheltuieli = [t for t in self.tranzactii if isinstance(t, Cheltuiala)]
        cheltuieli_sortate = sorted(cheltuieli, key=lambda t: t.suma, reverse=True)
        return cheltuieli_sortate[:n]

    def statistici_pe_categorii(self):
        categorii = {}
        for t in self.tranzactii:
            if isinstance(t, Cheltuiala):
                categorii[t.categorie] = categorii.get(t.categorie, 0) + t.suma
        return categorii

    def salveaza_json(self, fisier="date.json"):
        date = [t.to_dict() for t in self.tranzactii]
        with open(fisier, "w") as f:
            json.dump(date, f, indent=4)

    def incarca_json(self, fisier="date.json"):
        try:
            with open(fisier, "r") as f:
                date = json.load(f)
                self.tranzactii = []
                for d in date:
                    if d.get("tip") == "venit":
                        self.tranzactii.append(Venit(d["suma"], d["descriere"], d["sursa"]))
                    elif d.get("tip") == "cheltuiala":
                        self.tranzactii.append(Cheltuiala(d["suma"], d["descriere"], d["categorie"]))
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            self.tranzactii = []