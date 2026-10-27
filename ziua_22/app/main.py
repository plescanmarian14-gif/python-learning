from fastapi import*
from app.database import *
from app.routers import*

Base.metadata.create_all(bind=engine)

app=FastAPI(
    title="Gestor de Servicii APi",
    version="1.0.0",
    description="Sunt mare"
)
app.include_router(clienti.router)
app.include_router(tichete.router)

@app.get("/")
def root():
    return {"mesaj":"Gestionare Servicii este acum!"}