from fastapi import HTTPException
from app.services.avaliacao_service import create_avaliacao_service, get_avaliacoes_service, get_avaliacao_by_id_service

def create_avaliacao_controller(data):
    try:
        avaliacao = create_avaliacao_service(data)
        return {"message": "Avaliação criada com sucesso", "avaliacao": avaliacao}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

def get_avaliacoes_controller():
    try:
        avaliacoes = get_avaliacoes_service()
        return {"message": "Avaliações listadas com sucesso", "avaliacoes": avaliacacoes}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

def get_avaliacao_by_id_controller(id_avaliacao):
    try:
        return get_avaliacao_by_id_service(id_avaliacao)
    except LookupError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
