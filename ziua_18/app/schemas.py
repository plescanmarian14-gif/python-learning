from pydantic import BaseModel, Field
class CarteBase(BaseModel):
    titlu:str=Field(...,min_length=2,description="Titlul cartii")
    autor:str=Field(...,min_length=2,description="Autorul cartii")
    an_aparitie:int=Field(...,gt=0,description="Anul apartiei")
    disponibilitate:bool=True
class CarteCreate(CarteBase):
    pass
class CarteResponse(CarteBase):
    id:int

    class Config:
        from_attributes=True