
from app.repositories.professor_repository import *

def create_professor_service(data):
    return create_professor(data)

def get_professores_service():
    return get_all_professores()

def get_professor_by_id_service(id_professor):
    return get_professor_by_id(id_professor)

def update_professor_service(id_professor, data):
    return update_professor(id_professor, data)

def delete_professor_service(id_professor):
    return delete_professor(id_professor)

