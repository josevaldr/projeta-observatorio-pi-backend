from app.repositories.empresa_repository import (
    create_empresa,
    get_all_empresas,
    get_empresa_by_id,
    update_empresa,
    delete_empresa
)

from app.repositories.user_repository import get_user_by_id


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
