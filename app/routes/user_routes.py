from fastapi import APIRouter, HTTPException
from app.schemas.user_schemas import UserCreate, UserLogin
from app.controllers.user_controller import (
    create_user_controller,
    get_users_controller,
    get_user_by_id_controller,
    update_user_controller,
    delete_user_controller,
    authenticate_user_controller
)


router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/login")
def login(data: UserLogin):
    return authenticate_user_controller(data.email, data.senha)


@router.post("/")
def create_user(data: UserCreate):
    return create_user_controller(data)

@router.get("/{id}")
def get_user(id: int):
    return get_user_by_id_controller(id)


@router.put("/{id}")
def update_user(id: int, data: UserCreate):
    return update_user_controller(id, data)


@router.delete("/{id}")
def delete_user(id: int):
    return delete_user_controller(id)

