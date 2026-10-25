from fastapi import FastAPI
from app.database import engine,Base
from app.routers import categorii,produse

from app.database import engine, Base

Base.metadate.create_all(bind=engine)

app=FastAPI(
    title="Magazin Api",
    description="Api cu relatii",
    version="1.0.0"
)
app.inlcude_router(categorii.router)
app.include_router(produse.router)
@app.get("/")
def root():
    return {"mesaj":"Api functioneaza!"}