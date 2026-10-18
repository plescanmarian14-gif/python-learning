from fastapi import APIRouter,HTTPException,status
from typing import List,Optional

from app.schemas import CarteResponse
from app1.schemas import ProdusResponse,ProdusCreate
from app1.database import baza_de_date
import app1.database as db
router=APIRouter(
    prefix="/produse"
)

@router.get("/produse",response_model=List[ProdusResponse])
def returneaza(
    categorie:Optional[str]=None
):
    rezultat=baza_de_date
    if categorie:
        rezultat=[c for c in rezultat if categorie.lower() in c.categorie.lower()]
    return rezultat

@router.post("/produse", response_model=ProdusCreate,status_code=status.HTTP_201_CREATED)
def adauga(produs:ProdusCreate):
    nou=db.id_counter
    db.id_counter+=1
    produs=ProdusCreate(id=nou,**produs.model_dump())
    baza_de_date.append(produs)
    return produs
@router.get("/produse/{produs_id}")
def gasire(produs_id:int):
    for produs in baza_de_date:
        if produs.id==produs_id:
            return produs
    raise HTTPException(status_code=404, detail="Produs negasit!")



