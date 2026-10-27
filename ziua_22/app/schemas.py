from pydantic import *

class ClientCreare(BaseModel):
    nume:str=Field(min_length=2)
    email:str
class ClientResponse(ClientCreare):
    id:int
    class Config:
        from_attributes=True

class TichetCreate(BaseModel):
    titlu:str=Field(min_length=3)
    descriere:str
    urgent:bool=Field(default=False)
    client_id:int
class TichetResponse(TichetCreate):
    id:int
    client:ClientResponse
    class Config:
        from_attributes=True