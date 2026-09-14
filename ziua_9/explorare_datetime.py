from datetime import datetime, date

if __name__ == "__main__":
    # 1. Afișăm data și ora curentă formatată frumos
    acum = datetime.now()
    print(f"Data și ora curentă: {acum.strftime('%d-%m-%Y %H:%M:%S')}")
    print("-" * 40)

    # 2. Preluăm o dată de la utilizator
    print("Introduceți o dată din trecut pentru calcul.")
    zi = int(input("Ziua (1-31): "))
    luna = int(input("Luna (1-12): "))
    an = int(input("Anul (ex: 2000): "))

    # Creăm obiectul date pentru data introdusă și pentru data de azi
    data_user = date(an, luna, zi)
    data_azi = date.today()

    # 3. Calculăm diferența (rezultă un obiect timedelta)
    diferenta = data_azi - data_user

    # 4. Afișăm rezultatul
    if diferenta.days > 0:
        print(f"\nDe la data de {data_user.strftime('%d.%m.%Y')} au trecut {diferenta.days} zile.")
    elif diferenta.days == 0:
        print("\nData introdusă este chiar ziua de azi!")
    else:
        print(f"\nData introdusă este în viitor (peste {abs(diferenta.days)} zile).")