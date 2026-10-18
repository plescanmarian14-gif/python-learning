from fastapi import FastAPI
from app1.routers import produse

app=FastAPI(title="Produse de vanzare!")
app.include_router(produse.router)

@app.get("/")
def mesaj():
    return {"mesaj":"Vei reusi!"}