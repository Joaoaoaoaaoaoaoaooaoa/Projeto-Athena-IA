from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.database.connection import get_db
from backend.api.deps import get_current_user
from backend.models.user import User
from backend.models.task import Task
from backend.schemas.task import TaskCreate, TaskUpdate, TaskResponse

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.post("/", response_model=TaskResponse, status_code=201)
def create(data: TaskCreate, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    task = Task(user_id=user.id, **data.model_dump())
    db.add(task); db.commit(); db.refresh(task)
    return task

@router.get("/", response_model=list[TaskResponse])
def list_tasks(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return db.query(Task).filter(Task.user_id == user.id).order_by(Task.id.desc()).all()

@router.patch("/{task_id}", response_model=TaskResponse)
def update(task_id: int, data: TaskUpdate, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    task = db.query(Task).filter(Task.id == task_id, Task.user_id == user.id).first()
    if not task: raise HTTPException(404, "Tarefa não encontrada.")
    for key, value in data.model_dump(exclude_unset=True).items(): setattr(task, key, value)
    db.commit(); db.refresh(task)
    return task

@router.delete("/{task_id}", status_code=204)
def delete(task_id: int, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    task = db.query(Task).filter(Task.id == task_id, Task.user_id == user.id).first()
    if not task: raise HTTPException(404, "Tarefa não encontrada.")
    db.delete(task); db.commit()
