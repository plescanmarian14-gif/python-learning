from manager import ManagerFinanciar
from tranzactii import Venit, Cheltuiala
from utils import citeste_numar

manager = ManagerFinanciar()
manager.incarca_json()

while True:
    print("\n--- MENIU FINANCE TRACKER ---")
    print("1. Adauga Venit")
    print("2. Adauga Cheltuiala")
    print("3. Afiseaza toate tranzactiile")
    print("4. Sterge tranzactie")
    print("5. Afiseaza sold si totale")
    print("6. Statistici pe categorii")
    print("7. Top cheltuieli")
    print("8. Filtreaza dupa categorie")
    print("9. Iesire")

    optiune = input("\nAlege o optiune (1-9): ").strip()

    try:
        if optiune == "1":
            suma = citeste_numar("Introdu suma venitului: ")
            descriere = input("Descriere: ")
            sursa = input("Sursa (ex: salariu, freelance): ")
            v = Venit(suma, descriere, sursa)
            manager.adauga_tranzactie(v)
            manager.salveaza_json()

        elif optiune == "2":
            suma = citeste_numar("Introdu suma cheltuielii: ")
            descriere = input("Descriere: ")
            categorie = input("Categorie (ex: mancare, chirie): ")
            c = Cheltuiala(suma, descriere, categorie)
            manager.adauga_tranzactie(c)
            manager.salveaza_json()

        elif optiune == "3":
            if not manager.tranzactii:
                print("Nu exista tranzactii inregistrate.")
            else:
                print("\n--- LISTA TRANZACTII ---")
                for index, t in enumerate(manager.tranzactii):
                    print(f"{index}. {t}")

        elif optiune == "4":
            if not manager.tranzactii:
                print("Nu exista tranzactii de sters.")
            else:
                for index, t in enumerate(manager.tranzactii):
                    print(f"{index}. {t}")
                idx = int(citeste_numar("Introdu indexul tranzactiei de sters: "))
                manager.sterge_tranzactie(idx)
                manager.salveaza_json()

        elif optiune == "5":
            print(f"\nTotal Venituri: {manager.total_venituri()} RON")
            print(f"Total Cheltuieli: {manager.total_cheltuieli()} RON")
            print(f"Sold Curent: {manager.sold()} RON")

        elif optiune == "6":
            stats = manager.statistici_pe_categorii()
            print("\n--- STATISTICI PE CATEGORII ---")
            for cat, suma in stats.items():
                print(f"{cat}: {suma} RON")

        elif optiune == "7":
            n = int(citeste_numar("Cate cheltuieli din top vrei sa vezi? "))
            top = manager.top_cheltuieli(n)
            print(f"\n--- TOP {n} CHELTUIELI ---")
            for t in top:
                print(t)

        elif optiune == "8":
            cat = input("Introdu categoria cautata: ")
            filtrate = manager.filtreaza_dupa_categorie(cat)
            print(f"\n--- CHELTUIELI DIN CATEGORIA '{cat}' ---")
            for t in filtrate:
                print(t)

        elif optiune == "9":
            manager.salveaza_json()
            print("Datele au fost salvate. La revedere!")
            break

        else:
            print("Opțiune invalida! Te rog sa alegi un numar de la 1 la 9.")

    except Exception as e:
        print(f"\nA aparut o eroare: {e}. Incearca din nou!")