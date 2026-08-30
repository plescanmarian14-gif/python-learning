ghicit=0
i, j = 10, 200
while ghicit<5:
    raspuns=input(f"NUmarul este intre {i} si {j}?")
    if raspuns=="Da":
        i=i+10
        j=j-10
    elif raspuns=="NU":
        print(f"indiciu numarul se afla intre {i} si {j}")
    ghicit+=1
raspuns=int(input(f"Spune un numar{i} si {j}?"))
if raspuns==123:
    print("felicitari ai ghicit!")
else:
    print("ai pierdut")