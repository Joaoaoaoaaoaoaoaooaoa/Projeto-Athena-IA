from pydantic import BaseModel, EmailStr

class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    active: bool
    model_config = {"from_attributes": True}
