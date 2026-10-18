from pydantic import BaseModel,Field

class CarteBase(BaseModel):
    titlu:str=Field(min_length=2)
    autor:str=Field(min_length=4)
    an_aparitie:int=Field(gt=0)
    disponibilitate:bool=True
class CarteCreate(CarteBase):
    pass

class CarteResponse(CarteBase):
    id:int