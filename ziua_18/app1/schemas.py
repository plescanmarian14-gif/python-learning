from pydantic import BaseModel,Field

class ProdusBase(BaseModel):
    nume:str=Field(...,min_length=2,description="Introduceti nume")
    pret:float=Field(gt=0,description="Introduceti pretul")
    categorie:str=Field(description="Categorie:")
    in_stoc:bool=True

class ProdusCreate(ProdusBase):
    pass
class ProdusResponse(ProdusBase):
    id:int
