def function():
    while True:
        try:
            nr=input("Introduceti un numar: ")
            nr=int(nr)
            if nr<1 or nr>100:
                raise ValueError("Nu respecta intervalul 1 si 100")
        except ValueError as e:
            print(f"Eroare: {e}")
        else:
            print(f"Numarul ales este Corect! {nr}")
            break
        finally:
            print("Bloc executat!")
function()