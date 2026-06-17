
from app.repositories.professor_repository import *
from app.services.user_service import create_user_service
from app.schemas.user_schemas import UserCreate
from app.schemas.professor_schemas import ProfessorCreate

def create_professor_service(data):
    return create_professor(data)

def create_professor_completo_service(data):
    user_data = UserCreate(
        nome_usuario=data.nome_usuario,
        email=data.email,
        senha=data.senha,
        tipo_usuario="professor"
    )
    novo_usuario = create_user_service(user_data)
    
    prof_data = ProfessorCreate(
        id_professor=novo_usuario["id_usuario"],
        especialidade=data.especialidade
    )
    create_professor(prof_data)
    
    return {
        "id_professor": novo_usuario["id_usuario"],
        "nome_usuario": data.nome_usuario,
        "email": data.email,
        "especialidade": data.especialidade
    }



def get_professores_service():
    return get_all_professores()

def get_professor_by_id_service(id_professor):
    return get_professor_by_id(id_professor)

def update_professor_service(id_professor, data):
    return update_professor(id_professor, data)

def delete_professor_service(id_professor):
    return delete_professor(id_professor)

