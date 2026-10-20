from sqlalchemy import Column, Integer, String, Float, Boolean
from app.database import Base

class ProdusModel(Base):
    __tablename__ = "produse"  # Numele tabelei din SQLite

    id = Column(Integer, primary_key=True, index=True)
    nume = Column(String, index=True, nullable=False)
    pret = Column(Float, nullable=False)
    categorie = Column(String, index=True)
    in_stoc = Column(Boolean, default=True)
