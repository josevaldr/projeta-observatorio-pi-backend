from app.repositories.user_repository import (
    create_user,
    get_all_users,
    get_user_by_id,
    update_user,
    delete_user,
    get_user_by_email_and_password
)


def create_user_service(data):
    if not data.email:
        raise Exception("Email é obrigatório")

    return create_user(data)


def authenticate_user_service(email, senha):
    if not email:
        raise Exception("Email é obrigatório")
    if not senha:
        raise Exception("Senha é obrigatória")

    return get_user_by_email_and_password(email, senha)

def get_users_service():
    return get_all_users()


def get_user_by_id_service(user_id):
    return get_user_by_id(user_id)

def update_user_service(user_id, data):
    return update_user(user_id, data)

def delete_user_service(user_id):
    return delete_user(user_id)
