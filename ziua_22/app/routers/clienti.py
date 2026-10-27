from http.client import responses

from fastapi import*
from sqlalchemy.orm import*
from typing import*
from app.database import *
from app.models import*
from app.schemas import*

router=APIRouter(
    prefix="/clienti"
)
@router.post("",response_model=ClientResponse)
def cautare(
    client_in:ClientCreare,
    db:Session=Depends(get_db)
):
   exista=db.query(ClientModel).filter(ClientModel.email==client_in.email).first()
   if exista:
       raise HTTPException(status_code=400,detail="email exista deja")
   db_client=ClientModel(**client_in.model_dump())
   db.add(db_client)
   db.commit()
   db.refresh(db_client)

@router.get("",response_model=List[ClientResponse])
def afiasare(db:Session=Depends(get_db)):
    return db.query(ClientModel).all()

@router.delete("/{client_id}",response_model=ClientResponse)
def stergere(
        client_id:int,
        db:Session=Depends(get_db)
):
    exista=db.query(ClientModel).filter(ClientModel.id==client_id).first()
    if not exista:
        raise HTTPException(status_code=404,detail="nu a fost gasit")
    db.delete(exista)
    db.commit()