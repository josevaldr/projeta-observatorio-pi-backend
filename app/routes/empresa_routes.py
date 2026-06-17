from fastapi import APIRouter

from app.schemas.empresa_schemas import EmpresaCreate

from app.controllers.empresa_controller import (
    create_empresa_controller,
    get_empresas_controller,
    get_empresa_by_id_controller,
    update_empresa_controller,
    delete_empresa_controller
)


router = APIRouter(prefix="/empresas", tags=["Empresas"])


@router.get("")
def get_empresas():
    return get_empresas_controller()


@router.get("/{id_empresa}")
def get_empresa(id_empresa: int):
    return get_empresa_by_id_controller(id_empresa)


@router.post("")
def create_empresa(data: EmpresaCreate):
    return create_empresa_controller(data)


@router.put("/{id_empresa}")
def update_empresa(id_empresa: int, data: EmpresaCreate):
    return update_empresa_controller(id_empresa, data)


@router.delete("/{id_empresa}")
def delete_empresa(id_empresa: int):
    return delete_empresa_controller(id_empresa)
