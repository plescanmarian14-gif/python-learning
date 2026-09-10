import json

nume_fisier = "contacte.json"


def incarcare_contacte():
    try:
        with open(nume_fisier, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def salveaza_contacte(dic):
    try:
        # Corectat: encoding="utf-8", json.dump și indent=4
        with open(nume_fisier, "w", encoding="utf-8") as f:
            json.dump(dic, f, indent=4)
    except Exception as e:
        print(f"Eroare la salvare: {e}")


def agenda_contacte():
    dic = incarcare_contacte()

    while True:
        try:
            comanda = (
                input("\nAlege (adaugare/cautare/stergere/afisare/stop): ")
                .strip()
                .lower()
            )

            if comanda == "stop":
                print("La revedere!")
                break

            elif comanda == "adaugare":
                nume = input("Nume: ").strip()
                tel = input("Telefon: ").strip()

                # Corectat: .isdigit()
                if not tel.isdigit():
                    raise ValueError("Numărul de telefon trebuie să conțină doar cifre!")

                if nume in dic:
                    print("Există deja acest contact!")
                else:
                    dic[nume] = tel
                    salveaza_contacte(dic)
                    print("Contact adăugat și salvat cu succes!")

            elif comanda == "cautare":
                nume = input("Introduceți numele: ").strip()
                if nume in dic:
                    print(f"Numărul lui {nume} este: {dic[nume]}")
                else:
                    print("Numele nu există în agendă.")

            elif comanda == "stergere":
                nume = input("Introduceți numele: ").strip()
                if nume in dic:
                    del dic[nume]
                    salveaza_contacte(dic)
                    print("Contact șters cu succes!")
                else:
                    print("Numele nu există.")

            elif comanda == "afisare":
                if not dic:
                    print("Agenda este goală.")
                else:
                    print("\nAgenda ta:")
                    for nume, numar in dic.items():
                        print(f"Nume: {nume} | Tel: {numar}")
            else:
                print("Comandă necunoscută!")

        except ValueError as e:
            print(f"Eroare: {e}")


agenda_contacte()