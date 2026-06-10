from fastapi import HTTPException

from app.services.aluno_service import (
    create_aluno_service,
    get_alunos_service,
    get_aluno_by_id_service,
    update_aluno_service,
    delete_aluno_service
)


def create_aluno_controller(data):
    try:
        aluno = create_aluno_service(data)

        return {
            "message": "Aluno criado com sucesso",
            "aluno": aluno
        }

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


def get_alunos_controller():
    try:
        alunos = get_alunos_service()

        return {
            "message": "Alunos listados com sucesso",
            "alunos": alunos
        }

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


def get_aluno_by_id_controller(id_aluno):
    try:
        aluno = get_aluno_by_id_service(id_aluno)

        return {
            "message": "Aluno encontrado com sucesso",
            "aluno": aluno
        }

    except LookupError as e:
        raise HTTPException(status_code=404, detail=str(e))

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


def update_aluno_controller(id_aluno, data):
    try:
        return update_aluno_service(id_aluno, data)

    except LookupError as e:
        raise HTTPException(status_code=404, detail=str(e))

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


def delete_aluno_controller(id_aluno):
    try:
        return delete_aluno_service(id_aluno)

    except LookupError as e:
        raise HTTPException(status_code=404, detail=str(e))

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
