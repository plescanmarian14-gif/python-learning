from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional

from app.schemas import ProdusResponse
from app1.database import get_db
from app1.models import TastaturaModel
from app1.schemas import TastaturaResponse, TastaturaCreare

router=APIRouter(
    prefix=["/tastturi"],
    tags="Tastaturi Sql"
)

@router.post("",response_model=TastaturaResponse,status_code=status.HTTP_201_CREATED)
def adaugare(
        tastatura:TastaturaCreare,
        db:Session=Depends(get_db)
):
    db_tastatura=TastaturaModel(**tastatura.model_dump())
    db.add(db_tastatura)
    db.commit()
    db.refresh(db_tastatura)

    return db_tastatura

@router.get("",response_model=List[TastaturaResponse])
def citeste(
        wireless:Optional[bool]=None,
        db: Session = Depends(get_db)
):
    query=db.query(TastaturaModel)
    if wireless:
        query=query.filter(TastaturaModel.wireless==wireless)
    return query.all()

@router.delete("/{tastatura_id}",response_model=ProdusResponse)
def stergere(tastatura_id:int, db:Session=Depends(get_db)):
    tastatura=db.query(TastaturaModel).filter(TastaturaModel.id==tastatura_id).first()
    if not tastatura:
        raise HTTPException(status_code=404,detail="Eroare")
    db.delete(tastatura)
    db.commit()


