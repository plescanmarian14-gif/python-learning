from pydantic import BaseModel
from sqlalchemy import Column,Integer,String,Float,Boolean

class TastaturaModel(BaseModel):
    id=Column(Integer,PrimaryKey=True,Index=True)
    brand=Column(String,nullable=False)
    model=Column(String,nullable=False)
    pret=Column(Float,nullable=False)
    wireless=Column(Boolean,default=True)