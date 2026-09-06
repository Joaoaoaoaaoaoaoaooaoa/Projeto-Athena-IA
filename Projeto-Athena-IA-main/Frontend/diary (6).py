from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.database.connection import get_db
from backend.api.deps import get_current_user
from backend.models.user import User
from backend.models.diary import DiaryEntry
from backend.schemas.diary import DiaryCreate, DiaryResponse

router = APIRouter(prefix="/diary", tags=["Diary"])

@router.post("/", response_model=DiaryResponse, status_code=201)
def create(data: DiaryCreate, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    entry = DiaryEntry(user_id=user.id, content=data.content)
    db.add(entry); db.commit(); db.refresh(entry)
    return entry

@router.get("/", response_model=list[DiaryResponse])
def list_entries(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return db.query(DiaryEntry).filter(DiaryEntry.user_id == user.id).order_by(DiaryEntry.created_at.desc()).all()

@router.delete("/{entry_id}", status_code=204)
def delete(entry_id: int, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    entry = db.query(DiaryEntry).filter(DiaryEntry.id == entry_id, DiaryEntry.user_id == user.id).first()
    if not entry: raise HTTPException(404, "Registro não encontrado.")
    db.delete(entry); db.commit()
