from pydantic import BaseModel, Field

class RoutineCreate(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    description: str | None = None
    duration_minutes: int | None = Field(default=None, ge=1)

class RoutineUpdate(RoutineCreate):
    pass

class RoutineResponse(BaseModel):
    id: int
    title: str
    description: str | None
    duration_minutes: int | None
    model_config = {"from_attributes": True}
