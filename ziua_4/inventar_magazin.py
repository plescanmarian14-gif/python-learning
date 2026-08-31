def adauga_produs(**kwargs):
    nume=kwargs.get("nume")
    pret = kwargs.get("pret")
    cantitate = kwargs.get("cantitate")
    dicionar=kwargs.get("dicionar")
    dicionar["nume"]=nume
    dicionar["pret"] = pret
    dicionar["cantitate"] = cantitate
    total=int(pret)*int(cantitate)
    return dicionar,total

print( adauga_produs(dicionar={},nume="Marian",pret="20",cantitate="100"))