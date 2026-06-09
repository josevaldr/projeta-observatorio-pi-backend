from fastapi import HTTPException
from app.services.user_service import create_user_service

def create_user_controller(data):
    try:
        user = create_user_service(data)
        return {
            "message": "Usuário criado com sucesso",
            "data": user
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

