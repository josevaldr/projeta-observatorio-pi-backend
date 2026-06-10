
from fastapi import APIRouter

from app.schemas.aluno_schemas import AlunoCreate

from app.controllers.aluno_controller import (
    create_aluno_controller,
    get_alunos_controller,
    get_aluno_by_id_controller,
    update_aluno_controller,
    delete_aluno_controller
)


router = APIRouter(prefix="/alunos", tags=["Alunos"])


@router.post("/")
def create_aluno(data: AlunoCreate):
    return create_aluno_controller(data)


@router.get("/")
def get_alunos():
    return get_alunos_controller()


@router.get("/{id_aluno}")
def get_aluno(id_aluno: int):
    return get_aluno_by_id_controller(id_aluno)


@router.put("/{id_aluno}")
def update_aluno(id_aluno: int, data: AlunoCreate):
    return update_aluno_controller(id_aluno, data)


@router.delete("/{id_aluno}")
def delete_aluno(id_aluno: int):
    return delete_aluno_controller(id_aluno)
