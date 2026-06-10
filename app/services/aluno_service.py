from app.repositories.aluno_repository import (
    create_aluno,
    get_all_alunos,
    get_aluno_by_id,
    update_aluno,
    delete_aluno
)

from app.repositories.user_repository import get_user_by_id


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
