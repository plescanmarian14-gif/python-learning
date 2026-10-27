from sqlalchemy import Column,Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class ClasaModel(Base):
    __tablename__="clase"
    id=Column(Integer,primary_key=True,index=True)
    nume_clasa=Column(String,unique=True,nullable=False)
    elevi=relationship("ElevModel",back_populates="clasa")

class ElevModel(Base):
    __tablename__="elevi"
    id=Column(Integer,primary_key=True,index=True)
    nume_elev=Column(String,nullable=False)
    clasa_id=Column(Integer,ForeignKey("clase_id"),nullable=False)
    clasa=relationship("ClasaModel",back_populates="elevi")
