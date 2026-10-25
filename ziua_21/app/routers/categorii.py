from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.models import CategorieModel
from app.schemas import CategorieCreate, CategorieResponse

router=APIRouter(prefix="/categorii",tags=["Categorii"])

@router.post("",response_model=CategorieModel,status_code=status.HTTP_201_CREATED)
def adauga(
        cat_in:CategorieCreate,
        db:Session=Depends(get_db),
):
    exista=db.query(CategorieModel).filter(CategorieModel.nume==cat_in.nume).first()
    if exista:
        raise HTTPException(404,detail="Categorie exista deja")
    db_cat=CategorieModel(**cat_in.model_dump())
    db.add(db_cat)
    db.commit()
    db.refresh(db_cat)
    return db_cat
@router.get("",response_model=List[CategorieResponse])
def citeste_categorii(db:Session=Depends(get_db)):
    return db.query(CategorieModel).all()
