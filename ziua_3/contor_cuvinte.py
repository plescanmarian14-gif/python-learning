from collections import Counter
exprese=str(input("Introduceti o propozitie: "))
print(Counter(exprese))

cuvinte = exprese.split(" ")
dictionar={}
for i in range (len(cuvinte)-1):
    nr=1
    for j in range(i+1,len(cuvinte)):
        if cuvinte[i]==cuvinte[j]:
            nr+=1
    dictionar[cuvinte[i]]=nr
dictionar[cuvinte[i]]+=1
print(dictionar)
