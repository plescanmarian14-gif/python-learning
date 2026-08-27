lista=[1,3,5,8,4]
max_nr=0
for i in range(len(lista)):
    if max_nr < lista[i] :
        max_nr=lista[i]
print(max_nr)