from fastapi import FastAPI
from app.routers import carte

app=FastAPI(
    title="Sistem Biblioteca Enterprice",
    version="1.0.0"
)

app.include_router(carte.router)

@app.get("/")
def root():
    return{"mesaj": "Api-ul functioneaza! Mergi la /docs pt doc"}