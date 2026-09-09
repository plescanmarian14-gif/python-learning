# 1. Clasa de bază
class Material:
    def __init__(self, titlu, autor, disponibila=True):
        self.titlu = titlu
        self.autor = autor
        self.disponibila = disponibila

    def descriere(self):
        stare = "Disponibil" if self.disponibila else "Împrumutat"
        return f"'{self.titlu}' de {self.autor} [{stare}]"


# 2. Clasele copii (moștenesc din Material)
class Carte(Material):
    def __init__(self, titlu, autor, nr_pagini, disponibila=True):
        super().__init__(titlu, autor, disponibila)
        self.nr_pagini = nr_pagini

    def descriere(self):
        return f"[Carte] {super().descriere()} - {self.nr_pagini} pagini"


class Revista(Material):
    def __init__(self, titlu, autor, numar_editie, disponibila=True):
        super().__init__(titlu, autor, disponibila)
        self.numar_editie = numar_editie

    def descriere(self):
        return f"[Revistă] {super().descriere()} - Ediția nr. {self.numar_editie}"


# 3. Clasa Biblioteca (Polimorfism practic)
class Biblioteca:
    def __init__(self):
        self.materiale = []

    def adauga_material(self, material):
        self.materiale.append(material)

    def imprumuta_carte(self, titlu):
        # Caută atât cărți, cât și reviste după titlu
        for m in self.materiale:
            if m.titlu.lower() == titlu.lower():
                if m.disponibila:
                    m.disponibila = False
                    print(f"Ai împrumutat cu succes: {m.titlu}")
                    return
                else:
                    print(f"Ne pare rău, '{m.titlu}' este deja împrumutat(ă).")
                    return
        print(f"Materialul '{titlu}' nu a fost găsit în bibliotecă.")

    def afiseaza_disponibile(self):
        print("\n--- Materiale disponibile ---")
        exista = False
        for m in self.materiale:
            if m.disponibila:
                print(m.descriere())  # Apel polimorfic!
                exista = True
        if not exista:
            print("Nu există materiale disponibile.")


# --- Testare ---

biblio = Biblioteca()

# Adăugăm ambele tipuri de materiale în aceeași listă
c1 = Carte("Poezii", "Mihai Eminescu", 250)
r1 = Revista("National Geographic", "Colectiv Redacțional", 102)

biblio.adauga_material(c1)
biblio.adauga_material(r1)

# Afișăm starea inițială
biblio.afiseaza_disponibile()

# Împrumutăm o Carte și o Revistă folosind ACEEAȘI metodă
print("\n--- Testare Împrumut ---")
biblio.imprumuta_carte("Poezii")             # Împrumută o carte
biblio.imprumuta_carte("National Geographic") # Împrumută o revistă

# Verificăm din nou ce a rămas disponibil
biblio.afiseaza_disponibile()