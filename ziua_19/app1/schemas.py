from pydantic import BaseModel,Field
class TastaturaBase(BaseModel):
    brand:str=Field(...,min_length=2,description="Minim 2 caractere")
    model:str=Field(...,min_length=1,description="Minim 1 caracter")
    pret:float=Field(gt=0)
    wireless:bool=True
class TastaturaCreare(TastaturaBase):
    pass
class TastaturaResponse(TastaturaBase):
    id:int
    class Config:
        from_attributes=True