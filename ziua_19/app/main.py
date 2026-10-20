from fastapi import FastAPI
from app.database import engine, Base
from app.routers import produse

# Această linie creează automat fișierul magazin.db și tabelele din models.py la pornire!
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Magazin API cu Baza de Date Reală")

app.include_router(produse.router)

@app.get("/")
def root():
    return {"mesaj": "API cu SQLite și SQLAlchemy este activ!"}