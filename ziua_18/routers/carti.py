from fastapi import APIRouter,HTTPException
from typing import List, Optional
from models import CarteCreate, CarteResponse

router=APIRouter(
    prefix="/carti",
    tags=["Carti"]
)

baza_de_date=[]
id_counter=1

@router.get("",response_model=List[CarteResponse])
def citeste_carti():
    return baza_de_date

@router.post("",response_model=CarteResponse)
def adauga_carte(carte:CarteCreate):
    global id_counter
    noua_carte=CarteResponse(id=id_counter,**carte.model_dump())
    id_counter+=1
    baza_de_date.append(noua_carte)
    return noua_carte
