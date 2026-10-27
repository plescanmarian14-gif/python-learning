from enum import unique
from http.client import HTTPException

from fastapi.openapi.utils import status_code_ranges
from sqlalchemy import Column,Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
from starlette.middleware.sessions import Session


class ScoaliModel(Base):
    __tablename__="scola"
    id=Column(Integer,primary_key=True,nullable=True)
    nume_scoala=Column(String, unique=True, nullable=False)
    elevi=relationship("EleviModel",back_populates="scoala")

class EleviModel(Base):
    __tablename__="elevi"
    id=Column(Integer,primary_key=True,nullable=True)
    nume_elev=Column(String,nullable=False)
    clasa_id=Column(Integer, ForeignKey("clasa_id"),nullable=False)
    scoala=relationship("ScoliModel",back_populates="elevi")

@router.post("/elevi",status_code=status.HTTP_201_CREATED)
def adauga_elev(elev_in:EleviModel,db:Session=Depends(get_db)):
    clasa_existenta=db.query(ClassModel).filter(elev_in.id==ClasaModel.id).first()
    if not clasa_existenta:
        raise HTTPException(404, "negasit")
    db_elev=EleviModel(**elev_in.model_dump())
    db.add(db_elev)
    db.commit()
    db.refresh(db_elev)
    return db_elev
