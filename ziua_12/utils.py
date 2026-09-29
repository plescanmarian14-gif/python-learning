def valideaza_suma(functie):
    def wrapper(self, suma, *args, **kwargs):
        if suma <= 0:
            raise ValueError("Suma trebuie sa fie un numar pozitiv!")
        return functie(self, suma, *args, **kwargs)
    return wrapper


def logheaza_actiune(functie):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Se executa actiunea: {functie.__name__}...")
        rezultat = functie(*args, **kwargs)
        print(f"[LOG] Actiune finalizata cu succes.")
        return rezultat
    return wrapper


def citeste_numar(mesaj):
    while True:
        try:
            valoare = float(input(mesaj))
            return valoare
        except ValueError:
            print("Eroare: Te rog sa introduci un numar valid!")