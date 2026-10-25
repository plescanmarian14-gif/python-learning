from pydoc import describe

from fastapi import FastAPI
from app.database import engine,Base
from app.routers import articole

Base.metadata.create_all(bind=engine)

app=FastAPI(
    title="Depozit",
    description="Sistem complet",
    version="1.0.0"
)

app.include_router(articole.router)

@app.get("/")
def root():
    return "Api functioneaza"