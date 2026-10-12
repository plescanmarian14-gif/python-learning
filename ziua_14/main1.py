from fastapi import FastAPI
app = FastAPI()

lista=["Ana","Marian"]

@app.get("/afisare")
def afisare():
    return{"mesaj":"Bine ati venit!","lista":lista}

@app.post("/metoda_post")
def adaugare(element:str):
    lista.append(element)
    return {"lista":lista}
@app.put("/metoda_put/{index}")
def modificare(index:int):
    if index <0 or index >len(lista):
        return {"eroare":"index gresit"}
    lista[index]="Mariafaf"
    return {"lista":lista}
@app.delete("/stergere/{index}")
def stergere(index:int):
    if index <0 or index >len(lista):
        return {"eroare":"index gresit"}
    element=lista.pop(index)
    return{
        "mesaj": element,
        "lista":lista
    }

