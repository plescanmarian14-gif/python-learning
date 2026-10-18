from fastapi import FastAPI
from routers import carti

app=FastAPI(title="Sitem biblioteca Enterprice")
app.include_router(carti.router)