dictionar={}
while True:
    adaug=str(input("Adaug: Da sau Nu"))
    if adaug=="Da":
        nume=str(input("Introduceti numele: "))
        telefon=input("Introduceti numarul: ")
        dictionar[nume]=telefon
    elif adaug=="Nu":
        break
print(dictionar)

