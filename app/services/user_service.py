from app.repositories.user_repository import create_user

def create_user_service(data):
    if not data.email:
        raise Exception("Email é obrigatório")

    return create_user(data)
