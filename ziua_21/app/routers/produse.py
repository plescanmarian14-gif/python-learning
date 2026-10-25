from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.models import ProdusModel,CategorieModel
from app.schemas import ProdusCreate,ProdusResponse

router=APIRouter(Prefix="/produse",tags=["Produse"])

@router.post("",response_model=ProdusResponse,status_code==status.HTTP_201_CREATED)
def adauga(
    produs_int:ProdusCreate,
    db:Session=Depends(get_db)
):
    exista=db.query(ProdusModel).filter(CategorieModel.categorie_id==produs_in.categorie_id).first()
    if not exista:
        raise HTTPException(
            404,detail="categoie specifica nu exista"
        )
    produs=ProdusModel(**produs_in.model_dump())
    db.add(produs)
    db.commit()
    db.refresh(produs)
    return produs