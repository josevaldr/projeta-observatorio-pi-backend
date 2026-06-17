from app.repositories.empresa_repository import (
    create_empresa,
    get_all_empresas,
    get_empresa_by_id,
    update_empresa,
    delete_empresa
)

from app.repositories.user_repository import get_user_by_id
from app.services.user_service import create_user_service
from app.schemas.user_schemas import UserCreate
from app.schemas.empresa_schemas import EmpresaCreate


def create_empresa_service(data):
    usuario = get_user_by_id(data.id_empresa)

    if not usuario:
        raise ValueError("Usuário não encontrado. Crie o usuário antes de criar a empresa.")

    if usuario["tipo_usuario"] != "empresa":
        raise ValueError("O usuário precisa ser do tipo empresa.")

    empresa_existente = get_empresa_by_id(data.id_empresa)

    if empresa_existente:
        raise ValueError("Essa empresa já foi cadastrada.")

    return create_empresa(data)

def create_empresa_completo_service(data):
    user_data = UserCreate(
        nome_usuario=data.nome_usuario,
        email=data.email,
        senha=data.senha,
        tipo_usuario="empresa"
    )
    novo_usuario = create_user_service(user_data)
    
    emp_data = EmpresaCreate(
        id_empresa=novo_usuario["id_usuario"],
        telefone=data.telefone,
        cnpj=data.cnpj
    )
    create_empresa(emp_data)
    
    return {
        "id_empresa": novo_usuario["id_usuario"],
        "nome_usuario": data.nome_usuario,
        "email": data.email,
        "telefone": data.telefone,
        "cnpj": data.cnpj
    }


def get_empresas_service():
    return get_all_empresas()


def get_empresa_by_id_service(id_empresa):
    empresa = get_empresa_by_id(id_empresa)

    if not empresa:
        raise LookupError("Empresa não encontrada.")

    return empresa


def update_empresa_service(id_empresa, data):
    empresa = get_empresa_by_id(id_empresa)

    if not empresa:
        raise LookupError("Empresa não encontrada.")

    return update_empresa(id_empresa, data)


def delete_empresa_service(id_empresa):
    empresa = get_empresa_by_id(id_empresa)

    if not empresa:
        raise LookupError("Empresa não encontrada.")

    return delete_empresa(id_empresa)
