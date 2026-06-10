
from app.repositories.coordenador_repository import *

def create_coordenador_service(data):
    return create_coordenador(data)

def get_coordenadores_service():
    return get_all_coordenadores()

def get_coordenador_by_id_service(id_coordenador):
    return get_coordenador_by_id(id_coordenador)

def update_coordenador_service(id_coordenador, data):
    return update_coordenador(id_coordenador, data)

def delete_coordenador_service(id_coordenador):
    return delete_coordenador(id_coordenador)
