from pydantic import BaseModel, Field
from typing import List, Optional

class CategorieBase(BaseModel):
    nume:str=Field(...,min_length=3)

class CategorieCreate(CategorieBase):
    pass

class CategorieResponse(CategorieBase):
    id:int

    class Config:
        from_attributes=True

class ProdusBase(BaseModel):
    nume:str=Field(...,min_length=3)
    pret:float=Field(...,gt=0)
    categorie_id:int
class ProdusCreate(ProdusBase):
    pass
class ProdusResponse(ProdusBase):
    id:int
    categorie:CategorieResponse
    class Config:
        from_attributes=True
