lista_cumparaturi=[]
while True:
    produs=input("Introduceti produs(sau stop daca vreti sa opriti):")
    if produs.lower() == "stop":
        break
    lista_cumparaturi.append(produs)
print(f"Lista este :{lista_cumparaturi}")