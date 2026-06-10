
from fastapi import APIRouter
from app.controllers.professor_controller import *
from app.schemas.professor_schemas import ProfessorCreate

router = APIRouter(prefix="/professores", tags=["Professores"])

@router.post("/")
def create_professor(data: ProfessorCreate):
    return create_professor_controller(data)

@router.get("/")
def get_professores():
    return get_professores_controller()

@router.get("/{id}")
def get_professor(id: int):
    return get_professor_by_id_controller(id)

@router.put("/{id}")
def update_professor(id: int, data: ProfessorCreate):
    return update_professor_controller(id, data)

@router.delete("/{id}")
def delete_professor(id: int):
    return delete_professor_controller(id)
