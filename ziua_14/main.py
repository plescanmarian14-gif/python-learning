from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="Task Manager API")


# 1. Definim modelul de date cu Pydantic
class Task(BaseModel):
    id: int
    titlu: str
    descriere: Optional[str] = None
    finalizat: bool = False


# "Baza de date" în memorie
db_tasks: List[Task] = []


# 2. Endpoint GET - Primirea tuturor sarcinilor
@app.get("/tasks", response_model=List[Task])
def get_tasks():
    return db_tasks


# 3. Endpoint POST - Adăugarea unei sarcini noi
@app.post("/tasks", response_model=Task)
def create_task(task: Task):
    # Verificăm dacă ID-ul există deja
    for t in db_tasks:
        if t.id == task.id:
            raise HTTPException(status_code=400, detail="Task-ul cu acest ID există deja!")

    db_tasks.append(task)
    return task


# 4. Endpoint GET după ID
@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    for task in db_tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task-ul nu a fost găsit")