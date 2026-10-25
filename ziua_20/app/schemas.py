from pydantic import BaseModel,Field

class ArticolBase(BaseModel):
    nume:str=Field(ge=2)
    cod_bare:str=Field(ge=5)
    pret:float=Field(gt=0)
    stoc:int=Field(ge=0)
    activ:bool=True
class ArticoleCreate(ArticolBase):
    pass
class ArticoleResponse(ArticolBase):
    id:int
    class Config:
        from_attributes=True