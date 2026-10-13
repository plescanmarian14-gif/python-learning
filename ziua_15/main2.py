from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional, List


app = FastAPI()

class Utilizator(BaseModel):
    id:int
    nume:str=Field(min_length=2,max_length=30,description="Trebuie intre 2-30 caractere")
    varsta:int=Field(gt=0,description="Varsta trebuie sa fie mai mare decat 0")
    email:str
    este_activ:bool=True

baza_de_date_produse: List[Utilizator]=[]
@app.get("/utilizatori")
def afisare():
    return baza_de_date_produse

@app.post("/utilizatori")
def adauga(u1_id:Utilizator):
    for i in baza_de_date_produse:
        if i.id==u1_id.id:
            raise HTTPException(status_code=400,detail="ID deja exista!")
    baza_de_date_produse.append(u1_id)
    return baza_de_date_produse
@app.get("/utilizatori/{user_id}")
def afisare_user(user_id:int):
    for i,p in enumerate (baza_de_date_produse):
        if p.id==user_id:
            return baza_de_date_produse[i]
    raise HTTPException(status_code=404,detail="Nu exista!")