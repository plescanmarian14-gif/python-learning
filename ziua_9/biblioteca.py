from materiale import *


class Biblioteca:
    def __init__(self):
        # Inițializăm lista de materiale ca atribut al clasei
        self.materiale = []

    def adauga(self):
        c1 = Material("Marian", "Paul", True)
        self.materiale.append(c1)

        c2 = Carte("Marian", "Paul", True, 300)
        self.materiale.append(c2)

        c3 = Revista("Marian", "Paul", True, 3)
        self.materiale.append(c3)  # Corectat din c2 în c3



# Exemplu de utilizare:
if __name__ == "__main__":
    b = Biblioteca()
    b.adauga()
    print(f"Număr de materiale în bibliotecă: {len(b.materiale)}")