from http.client import responses

from fastapi import*
from sqlalchemy.orm import*
from typing import*
from app.database import get_db
from app.models import*
from app.schemas import*

router=APIRouter(
    prefix="/tichete"
)

@router.post("",response_model=TichetResponse)
def adauga(
        client_in:TichetCreate,
        db:Session=Depends(get_db)
):
    exista=db.query(TichetModel).filter(TichetModel.id==client_in.id).first()
    if not exista:
        raise HTTPException(status_code=404,detail="not found")
    db_tichete=TichetModel(**client_in.model_dump())
    db.add(db_tichete)
    db.commit()
    db.refresh(db_tichete)
    return db_tichete

@router.get("",response_model=List[TichetResponse])
def afisare(db:Session=Depends(get_db)):
    return db.query(ClientModel).all()

@router.get("/{tichet_id}",response_model=TichetResponse)
def afisare(
        tichet_id:int,
        db:Session=Depends(get_db)
):
    exista=db.query(TichetModel).filter(TichetModel.id==tichet_id).first()
    if not exista:
        raise HTTPException(status_code=404,detail="nu e ")
    return exista