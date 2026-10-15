from typing import Optional, List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Magazin Biblioteca")

# 1. MODEL PYDANTIC
class Carte(BaseModel):
    id: int
    titlu: str = Field(min_length=2, description="Titlul cărții (minim 2 caractere)")
    autor: str = Field(min_length=3, description="Numele autorului (minim 3 caractere)")
    an_aparitie: int = Field(gt=0, description="Anul apariției trebuie să fie un număr pozitiv")
    disponibilitate: bool = True

# 2. BAZA DE DATE ÎN MEMORIE
baza_de_date: List[Carte] = [
    Carte(id=1, titlu="Laptop Gaming", autor="Mirel", an_aparitie=2003, disponibilitate=True),
    Carte(id=2, titlu="Laptop", autor="Mirela", an_aparitie=2024, disponibilitate=True)
]

@app.get("/carti",response_model=List[Carte])
def citeste(
    autor:Optional[str]=None,
    an_minim: Optional[int]=None
):
    rezultat=baza_de_date
    if autor:
        rezultat=[c for c in rezultat if autor.lower() in c.autor.lower()]
    if an_minim:
        rezultat=[c for c in rezultat if c.an_aparitie>=an_minim]
    return rezultat

# 4. READ ONE (Căutare după ID)
@app.get("/carti/{carte_id}", response_model=Carte)
def cauta_carte(carte_id: int):
    for carte in baza_de_date:
        if carte.id == carte_id:
            return carte
    raise HTTPException(status_code=404, detail="Cartea nu a fost găsită!")

# 5. CREATE (Adăugare carte nouă)
@app.post("/carti", response_model=Carte)
def adauga_carte(carte: Carte):
    for c in baza_de_date:
        if c.id == carte.id:
            raise HTTPException(status_code=400, detail="ID-ul există deja!")
    baza_de_date.append(carte)
    return carte

# 6. UPDATE (Modificare carte existentă)
@app.put("/carti/{carte_id}", response_model=Carte)
def modifica_carte(carte_id: int, carte_noua: Carte):
    for index, carte in enumerate(baza_de_date):
        if carte.id == carte_id:
            baza_de_date[index] = carte_noua
            return carte_noua
    raise HTTPException(status_code=404, detail="Cartea nu a fost găsită pentru modificare!")

# 7. DELETE (Ștergere carte)
@app.delete("/carti/{carte_id}")
def stergere_carte(carte_id: int):
    for index, carte in enumerate(baza_de_date):
        if carte.id == carte_id:
            del baza_de_date[index]
            return {"mesaj": f"Cartea cu ID-ul {carte_id} a fost ștersă!"}
    raise HTTPException(status_code=404, detail="Cartea nu a fost găsită pentru ștergere!")