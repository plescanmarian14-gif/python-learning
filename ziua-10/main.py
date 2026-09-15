persoane = [("Ana", 25), ("Bogdan", 19), ("Elena", 30)]
sortare=sorted(persoane,key=lambda p: p[1])
print(sortare)
filtru=list(filter(lambda p: p[1]>19,persoane))
print(filtru)