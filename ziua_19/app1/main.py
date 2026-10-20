from fastapi import FastAPI
from app1.database import engine, Base
from app1.routers import tastaturi

Base.metadata.create_all(bind=engine)
app=FastAPI(title="Tastaturi online")

app.include_router(tastaturi.router)

@app