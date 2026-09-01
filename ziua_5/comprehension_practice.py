patrate=[x**2 for x in range(1,21)]
print(patrate)
lista=[1,3,6,7,9,8]
div=[lista[i] for i in range(len(lista)) if lista[i]%3==0]
print(div)
text="Ana are mere"
text=text.split()
list1=[len(text[x]) for x in range(len(text))]
print(list1)
cuvinte = ["python", "code", "script"]
lungimi = {cuv: len(cuv) for cuv in cuvinte}
print(lungimi)

express=str(input("Introduceti o propozitie: "))
express=express.split()
cuvi={cuv: express.count(cuv) for cuv in express}
print(cuvi)