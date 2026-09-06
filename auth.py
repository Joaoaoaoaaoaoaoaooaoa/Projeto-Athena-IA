from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from backend.database.connection import get_db
from backend.models.user import User
from backend.schemas.auth import RegisterRequest, LoginRequest, TokenResponse
from backend.core.security import hash_password, verify_password, create_access_token

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register", response_model=TokenResponse, status_code=201)
def register(data: RegisterRequest, db: Session = Depends(get_db)):
    if len(data.password) < 8:
        raise HTTPException(400, "A senha deve ter pelo menos 8 caracteres.")
    if db.query(User).filter(User.email == data.email).first():
        raise HTTPException(409, "E-mail já cadastrado.")
    user = User(name=data.name.strip(), email=data.email.lower(), password_hash=hash_password(data.password))
    db.add(user); db.commit(); db.refresh(user)
    return TokenResponse(access_token=create_access_token(str(user.id)))

@router.post("/login", response_model=TokenResponse)
def login(data: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == data.email.lower()).first()
    if not user or not verify_password(data.password, user.password_hash):
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "E-mail ou senha inválidos.")
    return TokenResponse(access_token=create_access_token(str(user.id)))
