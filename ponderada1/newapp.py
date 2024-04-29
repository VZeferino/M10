from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from passlib.context import CryptContext
from pydantic import BaseModel

app = FastAPI(title="List")

# Usuários e suas senhas (simulando um banco de dados)
users_db = {
    "user1": "senha1",
    "user2": "senha2"
}

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
security = HTTPBasic()

def authenticate_user(credentials: HTTPBasicCredentials = Depends(security)):
    username = credentials.username
    password = credentials.password
    if username in users_db and pwd_context.verify(password, users_db[username]):
        return username
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Basic"},
        )

class Task(BaseModel):
    id: int
    title: str

tasks = []

@app.get("/tasks", response_model=list[Task])
def read_tasks(user: str = Depends(authenticate_user)):
    return tasks

@app.post("/tasks", response_model=Task)
def create_task(task: Task, user: str = Depends(authenticate_user)):
    task.id = len(tasks) + 1
    tasks.append(task)
    return task

@app.get("/tasks/{task_id}", response_model=Task)
def read_task(task_id: int, user: str = Depends(authenticate_user)):
    task = next((t for t in tasks if t.id == task_id), None)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, updated_task: Task, user: str = Depends(authenticate_user)):
    task = next((t for t in tasks if t.id == task_id), None)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    task.title = updated_task.title
    return task

@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, user: str = Depends(authenticate_user)):
    global tasks
    task = next((t for t in tasks if t.id == task_id), None)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    tasks = [t for t in tasks if t.id != task_id]
    return {"message": "Task deleted"}
