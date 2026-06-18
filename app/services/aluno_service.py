from app.repositories.aluno_repository import (
    create_aluno,
    get_all_alunos,
    get_aluno_by_id,
    update_aluno,
    delete_aluno,
    get_perfil_aluno,
    create_or_update_perfil_aluno,
    get_portfolio_by_username
)

from app.repositories.user_repository import get_user_by_id
from app.services.user_service import create_user_service
from app.schemas.user_schemas import UserCreate
from app.schemas.aluno_schemas import AlunoCreate


def create_aluno_service(data):
    usuario = get_user_by_id(data.id_aluno)

    if not usuario:
        raise ValueError("Usuário não encontrado. Crie o usuário antes de criar o aluno.")

    if usuario["tipo_usuario"] != "aluno":
        raise ValueError("O usuário precisa ser do tipo aluno.")

    aluno_existente = get_aluno_by_id(data.id_aluno)

    if aluno_existente:
        raise ValueError("Esse aluno já foi cadastrado.")

    return create_aluno(data)

def create_aluno_completo_service(data):
    # Passo 1: Criar o Usuário genérico
    user_data = UserCreate(
        nome_usuario=data.nome_usuario,
        email=data.email,
        senha=data.senha,
        tipo_usuario="aluno"
    )
    novo_usuario = create_user_service(user_data)
    
    # Passo 2: Criar o Aluno associado
    aluno_data = AlunoCreate(
        id_aluno=novo_usuario["id_usuario"],
        matricula=data.matricula,
        curso=data.curso,
        turma=data.turma
    )
    return create_aluno(aluno_data)



def get_alunos_service():
    return get_all_alunos()


def get_aluno_by_id_service(id_aluno):
    aluno = get_aluno_by_id(id_aluno)

    if not aluno:
        raise LookupError("Aluno não encontrado.")

    return aluno


def update_aluno_service(id_aluno, data):
    aluno = get_aluno_by_id(id_aluno)

    if not aluno:
        raise LookupError("Aluno não encontrado.")

    return update_aluno(id_aluno, data)


def delete_aluno_service(id_aluno):
    aluno = get_aluno_by_id(id_aluno)

    if not aluno:
        raise LookupError("Aluno não encontrado.")

    return delete_aluno(id_aluno)

def get_perfil_aluno_service(id_aluno):
    aluno = get_aluno_by_id(id_aluno)
    if not aluno:
        raise LookupError("Aluno não encontrado.")
    return get_perfil_aluno(id_aluno)

def create_or_update_perfil_aluno_service(id_aluno, data):
    aluno = get_aluno_by_id(id_aluno)
    if not aluno:
        raise LookupError("Aluno não encontrado.")
    return create_or_update_perfil_aluno(id_aluno, data)

def get_portfolio_by_username_service(username: str):
    portfolio = get_portfolio_by_username(username)
    if not portfolio:
        raise LookupError("Portfólio não encontrado.")
    return portfolio
