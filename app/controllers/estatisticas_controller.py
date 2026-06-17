from fastapi import HTTPException
from app.services.estatisticas_service import get_estatisticas_service

def get_estatisticas_controller():
    try:
        stats = get_estatisticas_service()
        return {
            "message": "Estatísticas carregadas com sucesso",
            "estatisticas": stats
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
