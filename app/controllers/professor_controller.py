
from fastapi import HTTPException
from app.services.professor_service import *

def create_professor_controller(data):
    try:
        return create_professor_service(data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


def get_professores_controller():
    try:
        return get_professores_service()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


def get_professor_by_id_controller(id_professor):
    try:
        professor = get_professor_by_id_service(id_professor)

        if not professor:
            raise HTTPException(status_code=404, detail="Professor não encontrado")

        return professor

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


def update_professor_controller(id_professor, data):
    try:
        return update_professor_service(id_professor, data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


def delete_professor_controller(id_professor):
    try:
        return delete_professor_service(id_professor)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
