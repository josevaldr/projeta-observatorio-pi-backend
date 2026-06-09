from fastapi import APIRouter
from app.controllers.user_controller import create_user_controller
from app.schemas.user_schemas import UserCreate

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/")
def create_user(data: UserCreate):
    return create_user_controller(data)
