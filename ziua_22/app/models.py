from sqlalchemy import *
from sqlalchemy.orm import relationship
from app.database import*
class ClientModel(Base):
    __tablename__="clienti"
    id=Column(Integer,primary_key=True,nullable=False)
    nume=Column(String,nullable=False)
    email=Column(String,unique=True,nullable=False)
    tichete=relationship("TichetModel",back_populates="clienti", cascade="all,delete-orphan")
class TichetModel(Base):
    __tablename__="tichete"
    id=Column(Integer,primary_key=True,index=False)
    titlu=Column(String,nullable=False)
    urgent=Column(Boolean, default=False)
    client_id=Column(Integer,ForeignKey("clienti.id"),nullable=False)
    client=relationship("ClientModel",back_populates="tichete")

