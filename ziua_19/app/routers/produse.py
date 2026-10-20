from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional

from app.database import get_db
from app.models import ProdusModel
from app.schemas import ProdusCreate, ProdusResponse

router = APIRouter(
    prefix="/produse",
    tags=["Produse SQL"]
)


# 1. READ ALL din Baza de Date
@router.get("", response_model=List[ProdusResponse])
def citeste_produse(
        categorie: Optional[str] = None,
        db: Session = Depends(get_db)
):
    query = db.query(ProdusModel)

    if categorie:
        query = query.filter(ProdusModel.categorie.ilike(f"%{categorie}%"))

    return query.all()


# 2. CREATE în Baza de Date
@router.post("", response_model=ProdusResponse, status_code=status.HTTP_201_CREATED)
def creeaza_produs(
        produs_in: ProdusCreate,
        db: Session = Depends(get_db)
):
    # Trecem datele din Pydantic în Modelul SQLAlchemy (fără manual ID, SQLite îl dă automat)
    db_produs = ProdusModel(**produs_in.model_dump())

    db.add(db_produs)  # Pregătim salvarea
    db.commit()  # Salvăm modificările pe disc
    db.refresh(db_produs)  # Încărcăm ID-ul generat automat

    return db_produs


# 3. READ ONE după ID
@router.get("/{produs_id}", response_model=ProdusResponse)
def citeste_produs(produs_id: int, db: Session = Depends(get_db)):
    produs = db.query(ProdusModel).filter(ProdusModel.id == produs_id).first()
    if not produs:
        raise HTTPException(status_code=404, detail="Produsul nu a fost găsit în baza de date!")
    return produs