
from app.repositories.coordenador_repository import *
from app.services.user_service import create_user_service
from app.schemas.user_schemas import UserCreate
from app.schemas.coordenador_schemas import CoordenadorCreate

def create_coordenador_service(data):
    return create_coordenador(data)

def create_coordenador_completo_service(data):
    user_data = UserCreate(
        nome_usuario=data.nome_usuario,
        email=data.email,
        senha=data.senha,
        tipo_usuario="coordenador"
    )
    novo_usuario = create_user_service(user_data)
    
    coord_data = CoordenadorCreate(
        id_coordenador=novo_usuario["id_usuario"],
        curso=data.curso
    )
    create_coordenador(coord_data)
    
    return {
        "id_coordenador": novo_usuario["id_usuario"],
        "nome_usuario": data.nome_usuario,
        "email": data.email,
        "curso": data.curso
    }


def get_coordenadores_service():
    return get_all_coordenadores()

def get_coordenador_by_id_service(id_coordenador):
    return get_coordenador_by_id(id_coordenador)

def update_coordenador_service(id_coordenador, data):
    return update_coordenador(id_coordenador, data)

def delete_coordenador_service(id_coordenador):
    return delete_coordenador(id_coordenador)
