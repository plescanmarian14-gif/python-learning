from fastapi import FastAPI
app=FastAPI()
nr=[4,5,10]

@app.get("/note")
def afisare():
    return {"note": nr}

@app.post("/adaugare/{index}")
def adaugare(index:int):
    if index<0 or index>10:
        return {"Eroare":"nota nu este buna!"}
    nr.append(index)
    return {"NOtele": nr}