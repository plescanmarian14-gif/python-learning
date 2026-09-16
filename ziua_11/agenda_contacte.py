import json
import os

FISIER_DB = "agenda.json"


# --- PERSISTENȚĂ JSON ---

def incarca_agenda(cale_fisier=FISIER_DB) -> dict:
    """Încarcă agenda din fișierul JSON. Returnează un dicționar gol dacă fișierul nu există."""
    if not os.path.exists(cale_fisier):
        return {}
    try:
        with open(cale_fisier, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError) as e:
        print(f"⚠️ Eroare la citirea fișierului: {e}. Se începe cu o agendă goală.")
        return {}


def salveaza_agenda(agenda: dict, cale_fisier=FISIER_DB) -> None:
    """Salvează dicționarul de contacte în format JSON."""
    try:
        with open(cale_fisier, "w", encoding="utf-8") as f:
            json.dump(agenda, f, indent=4, ensure_ascii=False)
        print("💾 Agenda a fost salvată cu succes.")
    except OSError as e:
        print(f"❌ Eroare la salvarea fișierului: {e}")


# --- FUNCȚIONALITĂȚI PRINCIPALE ---

def adauga_contact(agenda: dict) -> None:
    nume = input("Nume contact: ").strip()
    if not nume:
        print("❌ Numele nu poate fi gol.")
        return
    telefon = input("Număr telefon: ").strip()

    agenda[nume] = telefon
    salveaza_agenda(agenda)
    print(f"✅ Contactul '{nume}' a fost adăugat/actualizat.")


def cauta_partial(agenda: dict) -> None:
    """Căutare parțială după nume folosind filter + lambda."""
    termen = input("Introdu textul căutat în nume: ").strip().lower()
    if not termen:
        return

    # filter + lambda pentru a filtra cheile (numele) care conțin termenul căutat
    rezultate = list(filter(lambda nume: termen in nume.lower(), agenda.keys()))

    if rezultate:
        print(f"\n🔍 Rezultate găsite ({len(rezultate)}):")
        for nume in rezultate:
            print(f"  • {nume}: {agenda[nume]}")
    else:
        print("❌ Nu s-a găsit niciun contact care să potrivească căutării.")


def afiseaza_sortat(agenda: dict) -> None:
    """Afișează contactele sortate alfabetic după nume folosind sorted + lambda."""
    if not agenda:
        print("📂 Agenda este goală.")
        return

    # sorted + lambda (sortează tuplurile (nume, telefon) după nume, insensibil la majuscule)
    contacte_sortate = sorted(agenda.items(), key=lambda item: item[0].lower())

    print("\n📇 Lista contactelor (sortate alfabetic):")
    for nume, telefon in contacte_sortate:
        print(f"  • {nume}: {telefon}")


def sterge_contact(agenda: dict) -> None:
    nume = input("Numele contactului de șters: ").strip()
    if nume in agenda:
        del agenda[nume]
        salveaza_agenda(agenda)
        print(f"🗑️ Contactul '{nume}' a fost șters.")
    else:
        print("❌ Contactul nu există în agendă.")


# --- MENIU INTERACTIV ---

def meniu():
    agenda = incarca_agenda()

    while True:
        print("\n--- AGENDA CONTACTE ---")
        print("1. Adaugă / Modifică contact")
        print("2. Căutare parțială (filter + lambda)")
        print("3. Afișează toate contactele sortate (sorted + lambda)")
        print("4. Șterge contact")
        print("5. Ieșire")

        optiune = input("Alege opțiunea (1-5): ").strip()

        if optiune == "1":
            adauga_contact(agenda)
        elif optiune == "2":
            cauta_partial(agenda)
        elif optiune == "3":
            afiseaza_sortat(agenda)
        elif optiune == "4":
            sterge_contact(agenda)
        elif optiune == "5":
            print("La revedere!")
            break
        else:
            print("❌ Opțiune invalidă. Încearcă din nou.")


if __name__ == "__main__":
    meniu()