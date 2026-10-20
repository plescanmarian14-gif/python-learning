from pydantic import BaseModel, Field

class ProdusBase(BaseModel):
    nume: str = Field(..., min_length=2)
    pret: float = Field(..., gt=0)
    categorie: str
    in_stoc: bool = True

class ProdusCreate(ProdusBase):
    pass

class ProdusResponse(ProdusBase):
    id: int

    class Config:
        from_attributes = True  # Transformă modelul SQLAlchemy în JSON