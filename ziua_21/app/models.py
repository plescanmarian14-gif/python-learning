from sqlalchemy import Column,Integer,String,Float,ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class CategorieModel(Base):
    __tablename__="categorii"
    id=Column(Integer,primary_key=True,index=True)
    nume=Column(String,unique=True,nullable=False)
    produse=relationship("ProdusModel",back_populates="categorie")
class ProdusModel(Base):
    __table__="produse"
    id=Column(Integer,primary_key=True,index=True)
    nume=Column(String,nullable=False)
    pret=Column(Float,nullable=False)
    categorie_id=Column(Integer,ForeignKey("categorii.id"),nullable=False)
    categoie=relationship("CategorieModel",back_populates="produse")

