from fastapi import FastAPI
from backend.database.connection import engine
from backend.database.base import Base
from backend.api.auth import router as auth_router
from backend.api.tasks import router as tasks_router
from backend.api.routines import router as routines_router
from backend.api.diary import router as diary_router
from backend.api.users import router as users_router

app = FastAPI(title="Neuro Platform API", version="1.0.0")

app.include_router(auth_router)
app.include_router(users_router)
app.include_router(tasks_router)
app.include_router(routines_router)
app.include_router(diary_router)

@app.get("/")
def health():
    return {"application": "Neuro Platform API", "status": "online"}
