from enum import UNIQUE

from pydantic import BaseModel
from sqlalchemy import Column, Integer, Float, String, Boolean, PrimaryKeyConstraint


class ArticoleModel(BaseModel):
    id=Column(Integer,PrimaryKey=True,Index=True)
    nume=Column(String,nullable=False,Index=True)
    cod_bare=Column(String,nullable=False,UNIQUE=True)
    pret=Column(Float,nullable=False)
    stoc=Column(Integer,nullable=False,default=0)
    activ=Column(Boolean,default=True)
