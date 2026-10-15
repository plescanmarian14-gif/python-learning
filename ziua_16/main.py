from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional, List

app = FastAPI()

class Carte(BaseModel):
    id:int
    titlu:str=Field(min_length=2,description="Minim 2 caractere")
    autor:str=Field(min_length=3,description="Minim 3 caractere")
    an_aparitie:int=Field(gt=0,description="Mai mare decat 0")
    disponibilitate:bool=True
