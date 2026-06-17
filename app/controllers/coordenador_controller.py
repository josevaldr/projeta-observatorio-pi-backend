
from fastapi import HTTPException
from app.services.coordenador_service import *

def create_coordenador_controller(data):
    try:
        return create_coordenador_service(data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

def create_coordenador_completo_controller(data):
    try:
        coord = create_coordenador_completo_service(data)
        return {
            "message": "Usuário e Coordenador criados com sucesso!",
            "coordenador": coord
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))



def get_coordenadores_controller():
    try:
        return get_coordenadores_service()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


def get_coordenador_by_id_controller(id_coordenador):
    try:
        coord = get_coordenador_by_id_service(id_coordenador)

        if not coord:
            raise HTTPException(status_code=404, detail="Coordenador não encontrado")

        return coord

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


def update_coordenador_controller(id_coordenador, data):
    try:
        return update_coordenador_service(id_coordenador, data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


def delete_coordenador_controller(id_coordenador):
    try:
        return delete_coordenador_service(id_coordenador)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
