from fastapi import APIRouter,HTTPException,status
from typing import List,Optional
from app.schemas import CarteResponse,CarteCreate
from app.database import baza_de_date
import app.database as db

router=APIRouter(
    prefix="/carti",
    tags=["Carti/Carti API"]
)

@router.get("",response_model=List[CarteResponse])
def citeste_carti(
        q:Optional[str]=None,
        sortare:Optional[str]=None
):
    rezultat=baza_de_date
    if q:
        termen=q.lower()
        rezultat=[c for c in rezultat if termen in c.titlu.lower() or termen in c.autor.lower()]
    if sortare=="an":
        rezultat=sorted(rezultat,key=lambda x: x.an_apartie)
    return rezultat

@router.post("",response_model=CarteResponse,status_code=status.HTTP_201_CREATED)
def adauga(carte_in:CarteCreate):
    nou_id=db.id_counter
    db.id_counter+=1
    noua_carte=CarteResponse(id=nou_id,**carte_in.model_dump())
    baza_de_date.append(noua_carte)
    return noua_carte
@router.get("/{carte_id}",response_model=CarteResponse)
def citeste_carte(carte_id:int):
    for carte in baza_de_date:
        if carte.id==carte_id:
            return carte
    raise HTTPException(status_code=404,detail="Carte nu a fost gasita!")