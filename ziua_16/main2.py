from fastapi import FastAPI, HTTPException
from typing import List
from main import Carte
from models import Carte, baza_de_date

app=FastAPI(title="Magazin")
@app.get("/carti")
def afisare():
    return baza_de_date

@app.post("/carti")
def adauga(carte:Carte):
    for p in baza_de_date:
        if p.id==carte.id:
            raise HTTPException(status_code=400,detail="ID-ul exista deja")
    baza_de_date.append(carte)
    return carte
@app.get("/carti/{carte_id}")
def cautare(carte_id:int):
    for i,p in enumerate  (baza_de_date):
        if p.id==carte_id:
            return baza_de_date[i]
    raise HTTPException(status_code=404,detail="Cartea nu exista!")