from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.database.connection import get_db
from backend.api.deps import get_current_user
from backend.models.user import User
from backend.models.routine import Routine
from backend.schemas.routine import RoutineCreate, RoutineUpdate, RoutineResponse

router = APIRouter(prefix="/routines", tags=["Routines"])

@router.post("/", response_model=RoutineResponse, status_code=201)
def create(data: RoutineCreate, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    item = Routine(user_id=user.id, **data.model_dump())
    db.add(item); db.commit(); db.refresh(item)
    return item

@router.get("/", response_model=list[RoutineResponse])
def list_routines(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return db.query(Routine).filter(Routine.user_id == user.id).order_by(Routine.id.desc()).all()

@router.patch("/{routine_id}", response_model=RoutineResponse)
def update(routine_id: int, data: RoutineUpdate, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    item = db.query(Routine).filter(Routine.id == routine_id, Routine.user_id == user.id).first()
    if not item: raise HTTPException(404, "Rotina não encontrada.")
    for key, value in data.model_dump().items(): setattr(item, key, value)
    db.commit(); db.refresh(item)
    return item

@router.delete("/{routine_id}", status_code=204)
def delete(routine_id: int, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    item = db.query(Routine).filter(Routine.id == routine_id, Routine.user_id == user.id).first()
    if not item: raise HTTPException(404, "Rotina não encontrada.")
    db.delete(item); db.commit()
