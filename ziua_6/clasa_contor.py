class Contor:
    # Atribut de clasă (comun pentru toate obiectele)
    numar_instante = 0

    def __init__(self, nume):
        self.nume = nume  # Atribut de instanță

        # Incrementăm atributul de clasă la fiecare creare de obiect
        Contor.numar_instante += 1


print(f"Instanțe la început: {Contor.numar_instante}")

c1 = Contor("Primul")
print(f"După c1: {Contor.numar_instante}")

c2 = Contor("Al doilea")
c3 = Contor("Al treilea")
print(f"După c2 și c3: {Contor.numar_instante}")


print(f"Accesat din c1: {c1.numar_instante}")