lista = []

while True:
    x = input("Ce vrei să faci? adauga/sterge/arata/iesire: ")

    if x == "adauga":
        produs = input("Ce vrei să adaugi? ")
        lista.append(produs)

    elif x == "sterge":
        produs = input("Ce vrei să ștergi? ")
        if produs in lista:
            lista.remove(produs)
        else:
            print("Produsul nu există în listă.")

    elif x == "arata":
        print(lista)

    elif x == "iesire":
        break

    else:
        print("Comandă necunoscută.")