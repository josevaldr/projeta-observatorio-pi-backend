from fastapi import APIRouter

from app.schemas.aluno_schemas import AlunoCreate, AlunoCompletoCreate, PerfilAlunoCreate
from app.controllers.aluno_controller import *

router = APIRouter(prefix="/alunos", tags=["Alunos"])


@router.post("/")
def create_aluno(data: AlunoCreate):
    return create_aluno_controller(data)

@router.post("/completo")
def create_aluno_completo(data: AlunoCompletoCreate):
    return create_aluno_completo_controller(data)



@router.get("/")
def get_alunos():
    return get_alunos_controller()

@router.get("/publico/{nome_usuario}")
def get_portfolio_publico(nome_usuario: str):
    return get_portfolio_by_username_controller(nome_usuario)

@router.get("/{id_aluno}")
def get_aluno(id_aluno: int):
    return get_aluno_by_id_controller(id_aluno)


@router.put("/{id_aluno}")
def update_aluno(id_aluno: int, data: AlunoCreate):
    return update_aluno_controller(id_aluno, data)


@router.delete("/{id_aluno}")
def delete_aluno(id_aluno: int):
    return delete_aluno_controller(id_aluno)

@router.get("/{id_aluno}/perfil")
def get_perfil_aluno(id_aluno: int):
    return get_perfil_aluno_controller(id_aluno)

@router.put("/{id_aluno}/perfil")
def create_or_update_perfil_aluno(id_aluno: int, data: PerfilAlunoCreate):
    return create_or_update_perfil_aluno_controller(id_aluno, data)

