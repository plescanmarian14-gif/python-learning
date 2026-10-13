from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional, List

app = FastAPI()


# 1. Modelul Pydantic cu VALIDĂRI (Field)
class Produs(BaseModel):
    id: int
    nume: str = Field(min_length=3, max_length=50, description="Numele produsului (3-50 caractere)")
    pret: float = Field(gt=0, description="Prețul trebuie să fie mai mare decât 0")
    descriere: Optional[str] = None
    in_stoc: bool = True


baza_de_date_produse: List[Produs] = []


# 2. READ ALL (GET)
@app.get("/produse", response_model=List[Produs])
def citeste_produse():
    return baza_de_date_produse


# 3. READ ONE (GET după ID)
@app.get("/produse/{produs_id}", response_model=Produs)
def citeste_produs(produs_id: int):
    for p in baza_de_date_produse:
        if p.id == produs_id:
            return p
    raise HTTPException(status_code=404, detail="Produsul nu a fost găsit!")


# 4. CREATE (POST)
@app.post("/produse", response_model=Produs)
def adauga_produs(produs: Produs):
    for p in baza_de_date_produse:
        if p.id == produs.id:
            raise HTTPException(status_code=400, detail="ID-ul există deja!")

    baza_de_date_produse.append(produs)
    return produs


# 5. UPDATE (PUT)
@app.put("/produse/{produs_id}", response_model=Produs)
def modifica_produs(produs_id: int, produs_nou: Produs):
    for i, p in enumerate(baza_de_date_produse):
        if p.id == produs_id:
            baza_de_date_produse[i] = produs_nou
            return produs_nou

    raise HTTPException(status_code=404, detail="Produsul nu a fost găsit pentru modificare!")


# 6. DELETE
@app.delete("/produse/{produs_id}")
def stergere_produs(produs_id: int):
    for i, p in enumerate(baza_de_date_produse):
        if p.id == produs_id:
            del baza_de_date_produse[i]
            return {"mesaj": f"Produsul cu ID-ul {produs_id} a fost șters!"}

    raise HTTPException(status_code=404, detail="Produsul nu a fost găsit pentru ștergere!")