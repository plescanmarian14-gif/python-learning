dictionar={}
while True:
    client=input(" Alege adaugă produs, actualizează stoc, afișează tot inventarul, calculează valoarea totală a inventarului sau stop:")
    if client=="adaugă produs":
        nume = str(input("Introduceti numele: "))
        pret = input("Introduceti pret: ")
        dictionar[nume]=pret
    elif client=="actualizează stoc":
        nume = str(input("Introduceti numele: "))
        if nume in dictionar:
            pret = input("Introduceti pret: ")
            dictionar[nume]=pret
        else:
            print("produsul nu este in stoc")
    elif client=="afișează tot inventarul":
        print(dictionar)
    elif client=="calculează valoarea totală a inventarului":
        total=0
        for prets in dictionar.values():
            total+=prets
        print(f"Totalul este {total}")
    elif client=="stop":
        break
