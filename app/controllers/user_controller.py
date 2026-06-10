from fastapi import HTTPException
from app.services.user_service import (
    create_user_service,
    get_users_service,
    get_user_by_id_service,
    update_user_service,
    delete_user_service
)



def create_user_controller(data):
    try:
        user = create_user_service(data)
        return {
            "message": "Usuário criado com sucesso",
            "data": user
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


def get_user_by_id_controller(user_id):
    try:
        user = get_user_by_id_service(user_id)

        if not user:
            raise HTTPException(status_code=404, detail="Usuário não encontrado")

        return user

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


def update_user_controller(user_id, data):
    try:
        return update_user_service(user_id, data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    

def get_users_controller():
    try:
        users = get_users_service()
        return users

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
def delete_user_controller(user_id):
    try:
        return delete_user_service(user_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))    

